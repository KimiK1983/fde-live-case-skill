#!/usr/bin/env python3
"""Informational FDE preflight: WARN exits 0; invalid usage/project exits 2."""

from __future__ import annotations

import argparse
import locale
import os
import shutil
import subprocess
import sys
from pathlib import Path


def run(
    *command: str,
    timeout: int = 20,
    cwd: Path | None = None,
    clean_git_env: bool = False,
    clean_node_env: bool = False,
) -> tuple[bool, str, str]:
    env = os.environ.copy()
    if clean_git_env:
        env = {key: value for key, value in env.items() if not key.upper().startswith("GIT_")}
    if clean_node_env:
        env = {
            key: value
            for key, value in env.items()
            if key.upper() not in {"NODE_OPTIONS", "NODE_PATH"}
        }
    if os.name == "nt":
        env.setdefault("ProgramFiles", r"C:\Program Files")
        env.setdefault("ProgramData", r"C:\ProgramData")

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            check=False,
            cwd=cwd,
            encoding=locale.getpreferredencoding(False),
            env=env,
            errors="replace",
            text=True,
            timeout=timeout,
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        return False, "", str(error)

    stdout = result.stdout.strip()
    stderr = result.stderr.strip()
    if result.returncode != 0 and not stdout and not stderr:
        stderr = f"exit {result.returncode}"
    return result.returncode == 0, stdout, stderr


def first_line(output: str, fallback: str = "no output") -> str:
    return output.splitlines()[0] if output else fallback


def command_detail(stdout: str, stderr: str) -> str:
    detail = first_line(stdout or stderr)
    if stdout and stderr:
        detail += f"; stderr: {first_line(stderr)}"
    return detail


def show(label: str, state: str, detail: str) -> None:
    print(f"{label:<20} {state:<4} {detail}")


def check_version(
    label: str, command: str, *args: str, optional: bool = False
) -> tuple[str, str | None]:
    executable = shutil.which(command)
    if not executable:
        state = "INFO" if optional else "WARN"
        show(label, state, "not found")
        return state.lower(), None

    ok, stdout, stderr = run(
        executable,
        *args,
        clean_node_env=command in {"node", "npm", "pnpm"},
    )
    show(label, "OK" if ok else "WARN", command_detail(stdout, stderr))
    return ("ok" if ok else "warn"), executable


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--project",
        type=Path,
        required=True,
        help="repository or disposable project directory for the interview",
    )
    parser.add_argument(
        "--inspect-git",
        action="store_true",
        help="inspect Git metadata after reviewing and trusting the project",
    )
    parser.add_argument(
        "--probe-docker-daemon",
        action="store_true",
        help="contact the effective Docker daemon after confirming its target",
    )
    args = parser.parse_args(argv)
    project = args.project.resolve()
    if not project.is_dir():
        print(
            f"project             ERROR {project} is not a directory",
            file=sys.stderr,
        )
        return 2

    states = ["info"]
    print("FDE interview preflight")
    print("=======================")
    print(f"project              INFO {project}")

    git_state, git_executable = check_version("git", "git", "--version")
    states.append(git_state)
    for label, command, optional in (
        ("python", sys.executable, False),
        ("node", "node", False),
        ("npm", "npm", False),
        ("pnpm", "pnpm", True),
        ("uv", "uv", True),
    ):
        state, _ = check_version(
            label, command, "--version", optional=optional
        )
        states.append(state)

    docker_executable = shutil.which("docker")
    if not docker_executable:
        show("docker", "WARN", "CLI not found; keep a local run path")
        states.append("warn")
    else:
        cli_ok, stdout, stderr = run(docker_executable, "--version", timeout=5)
        show("docker CLI", "OK" if cli_ok else "WARN", command_detail(stdout, stderr))
        states.append("ok" if cli_ok else "warn")

        if not cli_ok:
            show("docker checks", "INFO", "skipped after CLI failure")
            states.append("info")
        elif not args.probe_docker_daemon:
            show(
                "docker daemon",
                "INFO",
                "not contacted; pass --probe-docker-daemon after confirming the target",
            )
            states.append("info")
        else:
            context = os.environ.get("DOCKER_CONTEXT")
            host = os.environ.get("DOCKER_HOST") if not context else None
            if context:
                target = f"context override {context}"
            elif host:
                target = "DOCKER_HOST override"
            else:
                target_ok, target, target_error = run(
                    docker_executable, "context", "show", timeout=5
                )
                if not target_ok:
                    show(
                        "docker target",
                        "WARN",
                        command_detail(target, target_error),
                    )
                    states.append("warn")
                    target = ""
                else:
                    target = f"context {first_line(target)}"

            if not target:
                show("docker checks", "INFO", "skipped; target is unknown")
                states.append("info")
                daemon_ok = None
            else:
                show("docker target", "INFO", target)
                states.append("info")
                daemon_ok, stdout, stderr = run(
                    docker_executable,
                    "info",
                    "--format",
                    "{{.ServerVersion}}",
                    timeout=5,
                )
                show(
                    "docker daemon",
                    "OK" if daemon_ok else "WARN",
                    command_detail(stdout, stderr),
                )
                states.append("ok" if daemon_ok else "warn")

            if daemon_ok is None:
                pass
            elif not daemon_ok:
                show("docker checks", "INFO", "skipped after daemon failure")
                states.append("info")
            else:
                ok, stdout, stderr = run(
                    docker_executable, "buildx", "version", timeout=5
                )
                show(
                    "docker buildx",
                    "OK" if ok else "WARN",
                    command_detail(stdout, stderr),
                )
                states.append("ok" if ok else "warn")

                ok, stdout, stderr = run(
                    docker_executable, "compose", "version", timeout=5
                )
                legacy_compose = shutil.which("docker-compose")
                if not ok and legacy_compose:
                    ok, stdout, stderr = run(legacy_compose, "version", timeout=5)
                show(
                    "docker compose",
                    "OK" if ok else "WARN",
                    command_detail(stdout, stderr),
                )
                states.append("ok" if ok else "warn")

                ok, containers, error = run(
                    docker_executable, "ps", "-q", timeout=5
                )
                if not ok:
                    show(
                        "running containers",
                        "WARN",
                        command_detail(containers, error),
                    )
                    states.append("warn")
                else:
                    count = len(containers.splitlines())
                    state = "OK" if count == 0 else "INFO"
                    detail = (
                        "0 active"
                        if count == 0
                        else f"{count} active; review only if they conflict with this case"
                    )
                    show("running containers", state, detail)
                    states.append(state.lower())

    if not git_executable:
        show("git working tree", "WARN", "git not found; use a disposable copy")
        states.append("warn")
    elif git_state != "ok":
        show("git working tree", "INFO", "skipped after Git CLI failure")
        states.append("info")
    elif not args.inspect_git:
        show(
            "git working tree",
            "INFO",
            "not inspected; pass --inspect-git after reviewing project metadata",
        )
        states.append("info")
    else:
        status_ok, changes, error = run(
            git_executable,
            "--no-optional-locks",
            "-c",
            "core.fsmonitor=false",
            "-C",
            str(project),
            "status",
            "--porcelain=v1",
            "--untracked-files=all",
            "--ignore-submodules=dirty",
            clean_git_env=True,
        )
        if status_ok:
            count = len(changes.splitlines())
            state = "OK" if count == 0 else "WARN"
            detail = (
                f"{count} Git-reported changed entries; submodule worktrees and "
                "assume-unchanged/skip-worktree files not inspected"
            )
        else:
            state = "WARN"
            detail = command_detail(changes, error)
        show("git working tree", state, detail)
        states.append(state.lower())

    print("-----------------------")
    print(
        f"OK={states.count('ok')} WARN={states.count('warn')} "
        f"INFO={states.count('info')}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
