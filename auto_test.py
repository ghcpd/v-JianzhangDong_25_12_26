import os
import subprocess
import sys

def run_tests():
    # Create logs directory if it doesn't exist
    os.makedirs('logs', exist_ok=True)

    # Run pytest with coverage
    # Use coverage to run pytest, including only app/ and omitting tests/
    cmd = [
        sys.executable, '-m', 'coverage', 'run', '--source=app', '--omit=tests/*',
        '-m', 'pytest', 'tests/', '-v'
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    print("Test output:")
    print(result.stdout)
    if result.stderr:
        print("Errors:")
        print(result.stderr)

    # Generate coverage report
    coverage_cmd = [sys.executable, '-m', 'coverage', 'report']
    coverage_result = subprocess.run(coverage_cmd, capture_output=True, text=True)

    # Write to log file
    with open('logs/test_run.log', 'w') as f:
        f.write("Test Run Results:\n")
        f.write("=" * 50 + "\n")
        f.write(result.stdout)
        if result.stderr:
            f.write("\nErrors:\n")
            f.write(result.stderr)
        f.write("\n\nCoverage Report:\n")
        f.write("=" * 50 + "\n")
        f.write(coverage_result.stdout)
        if coverage_result.stderr:
            f.write("\nCoverage Errors:\n")
            f.write(coverage_result.stderr)

    print("Coverage report written to logs/test_run.log")

if __name__ == "__main__":
    run_tests()