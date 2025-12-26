"""Run pytest and produce a coverage report for the project source (app/).

- Discovers and runs all tests under `tests/` using pytest
- Measures coverage with coverage.py for `app/` only
- Excludes the `tests/` directory from the coverage report
- Writes full output to `logs/test_run.log`
"""
from __future__ import annotations

import sys
import subprocess
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent
LOGS = ROOT / "logs"
LOG_FILE = LOGS / "test_run.log"
TESTS_DIR = ROOT / "tests"
SOURCE = "app"


def _write_log(text: str) -> None:
    LOGS.mkdir(parents=True, exist_ok=True)
    LOG_FILE.write_text(text, encoding="utf-8")


def _run(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)


def main() -> int:
    start = datetime.utcnow().isoformat() + "Z"
    header = f"Test run started: {start}\nCommand environment: {sys.executable}\n\n"

    out_lines = [header]

    # 1) Run tests under coverage if available
    cov_cmd = [sys.executable, "-m", "coverage", "run", "--source", SOURCE, "-m", "pytest", str(TESTS_DIR)]
    try:
        out_lines.append(f"Running: {' '.join(cov_cmd)}\n\n")
        res = _run(cov_cmd)
        out_lines.append(res.stdout or "(no output)\n")
        pytest_rc = res.returncode
    except FileNotFoundError:
        out_lines.append("coverage not installed or not runnable. Falling back to running pytest without coverage.\n\n")
        res = _run([sys.executable, "-m", "pytest", str(TESTS_DIR)])
        out_lines.append(res.stdout or "(no output)\n")
        pytest_rc = res.returncode

    # 2) If coverage is available, emit a coverage report that omits tests/
    try:
        report_cmd = [sys.executable, "-m", "coverage", "report", "--omit", "*/tests/*"]
        out_lines.append(f"\nGenerating coverage report: {' '.join(report_cmd)}\n\n")
        rep = _run(report_cmd)
        out_lines.append(rep.stdout or "(no output)\n")
    except FileNotFoundError:
        out_lines.append("coverage not available; skipped coverage report.\n")

    finish = datetime.utcnow().isoformat() + "Z"
    out_lines.append(f"\nTest run finished: {finish}\n")
    out_text = "\n".join(out_lines)

    _write_log(out_text)

    summary = [
        f"Wrote full test output + coverage to: {LOG_FILE}",
        f"pytest exit code: {pytest_rc}",
    ]
    print("\n".join(summary))

    return pytest_rc


if __name__ == "__main__":
    raise SystemExit(main())
