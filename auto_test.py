#!/usr/bin/env python
"""
Auto Test Runner - Discovers and runs all tests with coverage reporting.

This script:
1. Discovers and runs all test files under the tests/ folder using pytest
2. Measures code coverage using coverage.py (excluding tests/ directory)
3. Writes the final coverage report to logs/test_run.log
"""

import os
import sys
import subprocess
from pathlib import Path

def setup_logs_directory():
    """Create logs directory if it doesn't exist."""
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)
    return logs_dir

def run_tests_with_coverage():
    """Run all tests with coverage measurement."""
    logs_dir = setup_logs_directory()
    log_file = logs_dir / "test_run.log"

    print("=" * 70)
    print("Starting Test Discovery and Execution with Coverage Analysis")
    print("=" * 70)

    try:
        # Run pytest with coverage
        # Coverage will measure only app/ directory, excluding tests/
        cmd = [
            sys.executable,
            "-m",
            "pytest",
            "tests/",
            "--cov=app",
            "--cov-report=term-missing",
            "--cov-report=html:htmlcov",
            "-v",
        ]

        print(f"\nRunning command: {' '.join(cmd)}")
        print("-" * 70)

        # Run the command and capture output
        result = subprocess.run(cmd, capture_output=True, text=True)

        # Prepare the full output
        output = result.stdout + result.stderr

        # Print to console
        print(output)

        # Write to log file
        with open(log_file, "w") as f:
            f.write("=" * 70 + "\n")
            f.write("TEST EXECUTION AND COVERAGE REPORT\n")
            f.write("=" * 70 + "\n\n")
            f.write("Command: " + " ".join(cmd) + "\n\n")
            f.write("-" * 70 + "\n")
            f.write("OUTPUT:\n")
            f.write("-" * 70 + "\n")
            f.write(output)
            f.write("\n" + "=" * 70 + "\n")
            f.write(f"Exit Code: {result.returncode}\n")
            f.write("=" * 70 + "\n")

        print("\n" + "=" * 70)
        print(f"Coverage report written to: {log_file.resolve()}")
        print(f"HTML coverage report available in: {Path('htmlcov').resolve()}")
        print("=" * 70)

        return result.returncode

    except FileNotFoundError as e:
        error_msg = (
            f"Error: pytest not found. Please install pytest and coverage:\n"
            f"  pip install pytest pytest-cov coverage\n"
            f"Original error: {e}"
        )
        print(f"\n{error_msg}")

        # Write error to log file
        with open(log_file, "w") as f:
            f.write("ERROR\n")
            f.write(error_msg)

        return 1

    except Exception as e:
        error_msg = f"Unexpected error during test execution: {e}"
        print(f"\n{error_msg}")

        # Write error to log file
        with open(log_file, "w") as f:
            f.write("ERROR\n")
            f.write(error_msg)

        return 1

if __name__ == "__main__":
    exit_code = run_tests_with_coverage()
    sys.exit(exit_code)
