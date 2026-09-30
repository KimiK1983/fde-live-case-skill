"""Export exact candidate instructions, not an isolated runtime or a new skill."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


CANDIDATE_FILES = (
    "SKILL.md",
    "references/LIVE_CASE.md",
    "references/DECOMPOSITION.md",
    "references/AGENTIC.md",
)


def export_candidate(source: Path, brief: Path, output: Path) -> dict:
    source, brief, output = source.resolve(), brief.resolve(), output.resolve()
    if output == source or source in output.parents:
        raise ValueError("Export must be outside the source skill")
    if output.exists():
        raise FileExistsError("Export destination must not exist")
    if source in brief.parents and brief.parent != source / "practice/candidate":
        raise ValueError("Only practice/candidate briefs may be exported from the skill")
    payload = {}
    for name in CANDIDATE_FILES:
        path = (source / name).resolve()
        if source not in path.parents:
            raise ValueError(f"Source escapes skill: {name}")
        payload[name] = path.read_bytes()
    payload["case.md"] = brief.read_bytes()
    hashes = {name: hashlib.sha256(data).hexdigest() for name, data in payload.items()}
    instruction_hashes = {name: hashes[name] for name in CANDIDATE_FILES}
    manifest = {
        "format": 1,
        "instruction_version": hashlib.sha256(
            json.dumps(instruction_hashes, sort_keys=True).encode("utf-8")
        ).hexdigest(),
        "files": hashes,
        "isolation_verified": False,
        "semantic_review_required": True,
    }
    # Validate and read all inputs before creating any output. Never overwrite a view.
    output.mkdir(parents=True, exist_ok=False)
    for name, data in payload.items():
        target = output / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    (output / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--brief", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        manifest = export_candidate(args.skill_root, args.brief, args.output)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Export failed: {error}\n")
    print(f"Exported 5 files + manifest; version {manifest['instruction_version']}")
    print("Review contents and transfer to an isolated host; this command does not isolate access.")


if __name__ == "__main__":
    main()
