#!/usr/bin/env python3
"""Auto test runner.

- Discovers and runs tests under `tests/` using pytest.
- Measures coverage for `app/` only (excludes `tests/`).
- Writes coverage report to `logs/test_run.log`.
"""
import os
import subprocess
import sys

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "test_run.log")
PROJECT_TEST_DIR = "tests"
COVERAGE_SOURCE = "app"

os.makedirs(LOG_DIR, exist_ok=True)

python = sys.executable

# Run pytest under coverage for the specified source (app)
print("Running tests with coverage...")
run_cmd = [python, "-m", "coverage", "run", "--source", COVERAGE_SOURCE, "-m", "pytest", PROJECT_TEST_DIR]
proc = subprocess.run(run_cmd)
pytest_rc = proc.returncode

# Generate coverage report
report_cmd = [python, "-m", "coverage", "report", "-m"]
report_proc = subprocess.run(report_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
report_out = report_proc.stdout.decode("utf-8", errors="replace")

with open(LOG_FILE, "w", encoding="utf-8") as f:
    f.write(report_out)
    f.write("\n\n")
    f.write(f"pytest return code: {pytest_rc}\n")

print(f"Coverage report written to {LOG_FILE}")

# Exit with pytest's return code so CI can detect failures
sys.exit(pytest_rc)
