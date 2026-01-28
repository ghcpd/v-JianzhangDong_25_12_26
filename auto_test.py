"""
Run test discovery with pytest and produce a coverage report for the application source only.
- Discovers and runs tests under `tests/` with pytest
- Runs coverage for the `app/` package only and omits `tests/`
- Writes combined output to `logs/test_run.log`
"""
import os
import subprocess
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "test_run.log")
TEST_PATH = "tests"
SOURCE_PACKAGE = "app"

os.makedirs(LOG_DIR, exist_ok=True)

parts = []
parts.append(f"Test run started: {datetime.utcnow().isoformat()}Z")
parts.append("\n----- pytest output -----\n")

# Run pytest
pytest_proc = subprocess.run(["python", "-m", "pytest", TEST_PATH, "-q"], capture_output=True, text=True)
parts.append(pytest_proc.stdout)
if pytest_proc.stderr:
    parts.append("[pytest stderr]\n")
    parts.append(pytest_proc.stderr)

# Run coverage (limit to SOURCE_PACKAGE and explicitly omit tests/)
parts.append("\n----- coverage report -----\n")
coverage_cmd = [
    "coverage",
    "run",
    "--source=" + SOURCE_PACKAGE,
    "--omit=*/tests/*",
    "-m",
    "pytest",
    TEST_PATH,
]
cov_proc = subprocess.run(coverage_cmd, capture_output=True, text=True)
if cov_proc.returncode == 0:
    # get human-readable coverage report
    report_proc = subprocess.run(["coverage", "report", "-m"], capture_output=True, text=True)
    parts.append(report_proc.stdout)
    if report_proc.stderr:
        parts.append("[coverage stderr]\n")
        parts.append(report_proc.stderr)
else:
    parts.append("Coverage could not be run. Make sure `coverage` is installed.\n")
    parts.append(cov_proc.stdout or "")
    if cov_proc.stderr:
        parts.append("[coverage stderr]\n")
        parts.append(cov_proc.stderr)

# Summary and exit code
final_exit = pytest_proc.returncode or cov_proc.returncode
parts.append(f"\nTest run finished: {datetime.utcnow().isoformat()}Z\nExit code: {final_exit}\n")

# Write to log file
with open(LOG_FILE, "w", encoding="utf-8") as fh:
    fh.write("\n".join(parts))

print(f"Wrote test output to {LOG_FILE}")

# Exit with the combined return code
raise SystemExit(final_exit)
