"""Runner transport checks; do not call Codex or score model behavior."""

import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import run_regressions


class RunnerTests(unittest.TestCase):
    def test_cli_rejection_is_not_a_successful_response(self):
        with tempfile.TemporaryDirectory() as temporary:
            view = Path(temporary)
            rejection = subprocess.CompletedProcess([], 1, "", "HTTP 400: unsupported model")
            with patch.object(run_regressions.subprocess, "run", return_value=rejection):
                result = run_regressions.invoke("codex", view, "prompt")
            self.assertEqual(result["status"], "failed")
            self.assertEqual((view / "stage1.err").read_text(encoding="utf-8"), rejection.stderr)
            self.assertEqual((view / "stage1.md").read_text(encoding="utf-8"), "")

    def test_response_is_saved_without_claiming_semantic_success(self):
        event = {"type": "item.completed", "item": {"type": "agent_message", "text": "Respuesta no evaluada"}}
        with tempfile.TemporaryDirectory() as temporary:
            view = Path(temporary)
            response = subprocess.CompletedProcess([], 0, json.dumps(event) + "\n", "")
            with patch.object(run_regressions.subprocess, "run", return_value=response) as command:
                result = run_regressions.invoke("codex", view, "prompt")
            self.assertEqual(result["status"], "ok")
            self.assertNotIn("score", result)
            self.assertEqual((view / "stage1.md").read_text(encoding="utf-8"), event["item"]["text"])
            args = command.call_args.args[0]
            self.assertIn("gpt-6.1-sol", args)
            self.assertIn("model_reasoning_effort=medium", args)
            self.assertIn("read-only", args)

    def test_timeout_preserves_partial_trace(self):
        with tempfile.TemporaryDirectory() as temporary:
            view = Path(temporary)
            timeout = subprocess.TimeoutExpired(["codex"], 240, output=b"partial trace", stderr=b"partial error")
            with patch.object(run_regressions.subprocess, "run", side_effect=timeout):
                result = run_regressions.invoke("codex", view, "prompt")
            self.assertEqual(result["status"], "timeout")
            self.assertEqual((view / "stage1.jsonl").read_bytes(), b"partial trace")
            self.assertEqual((view / "stage1.err").read_bytes(), b"partial error")


if __name__ == "__main__":
    unittest.main()
