"""Replay four public, known regressions; not an isolated or blind benchmark."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "fde-live-case-skill/scripts"))
from export_candidate import export_candidate  # noqa: E402

EVIDENCE = ROOT / "evidence/gpt61-medium-2026-09-30"
CASES = ("arithmetic", "input-loss", "uncertain-write", "authoring")


def invoke(cli: str, view: Path, prompt: str) -> dict:
    args = [cli, "exec", "--ignore-user-config", "--skip-git-repo-check",
            "-m", "gpt-6.1-sol", "-c", "model_reasoning_effort=medium"]
    if os.name == "nt":
        args += ["-c", 'windows.sandbox="elevated"']
    args += ["-s", "read-only", "-C", str(view), "--json", "-"]
    start = time.monotonic()
    try:
        result = subprocess.run(args, input=prompt, capture_output=True, text=True,
                                encoding="utf-8", errors="replace", timeout=240)
    except subprocess.TimeoutExpired as error:
        for name, data in (("stage1.jsonl", error.stdout), ("stage1.err", error.stderr)):
            if data is not None:
                (view / name).write_bytes(data if isinstance(data, bytes) else data.encode("utf-8"))
        return {"status": "timeout", "seconds": round(time.monotonic() - start, 2)}
    (view / "stage1.jsonl").write_text(result.stdout, encoding="utf-8")
    (view / "stage1.err").write_text(result.stderr, encoding="utf-8")
    events = []
    for line in result.stdout.splitlines():
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            pass
    answers = [e["item"].get("text", "") for e in events
               if e.get("type") == "item.completed"
               and e.get("item", {}).get("type") == "agent_message"]
    answer = answers[-1] if answers else ""
    (view / "stage1.md").write_text(answer, encoding="utf-8")
    return {"status": "ok" if result.returncode == 0 and answer else "failed",
            "exit_code": result.returncode,
            "seconds": round(time.monotonic() - start, 2),
            "answer_length": len(answer)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="new results directory")
    parser.add_argument("--codex", default="codex", help="Codex executable, optionally absolute")
    args = parser.parse_args()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    version = subprocess.run([args.codex, "--version"], capture_output=True,
                             text=True, check=True).stdout.strip()
    (output / "environment.json").write_text(json.dumps({
        "cli": version, "model": "gpt-6.1-sol", "effort": "medium",
        "sandbox_requested": "read-only", "isolation_verified": False,
        "classification": "known regressions; manual evaluation; no A/B gain claim",
    }, indent=2) + "\n", encoding="utf-8")
    prompt = (EVIDENCE / "prompt.txt").read_text(encoding="utf-8")
    (output / "prompt.txt").write_text(prompt, encoding="utf-8")
    (output / "criteria.json").write_bytes((EVIDENCE / "criteria.json").read_bytes())

    def one(case: str) -> dict:
        view = output / case
        manifest = export_candidate(ROOT / "fde-live-case-skill", EVIDENCE / case / "case.md", view)
        result = invoke(args.codex, view, prompt)
        result["instruction_version"] = manifest["instruction_version"]
        (view / "result.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        print(case, result["status"], flush=True)
        return result

    with ThreadPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(one, CASES))
    print("Review commands/results and criteria manually; status ok only means the run completed.")
    return 0 if all(result["status"] == "ok" for result in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
