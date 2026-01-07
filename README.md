# Test Generation and Automation

This project now includes automated test generation and coverage reporting.

## Generated Files

### Test Files
The following test files were generated for previously untested modules in the `app/` directory:
- `tests/test_discount.py`: Tests for discount calculations.
- `tests/test_errors.py`: Tests for custom exception classes.
- `tests/test_permissions.py`: Tests for permission checking logic.
- `tests/test_utils.py`: Tests for utility functions.

### Report File
- `report.json`: A JSON file listing all untested modules that were addressed, along with their corresponding test files.

### Automation Script
- `auto_test.py`: A Python script that automates the testing process.

## Running Tests

To run all tests and generate coverage reports, execute the `auto_test.py` script:

```bash
python auto_test.py
```

This script will:
1. Run all test files in the `tests/` directory using pytest.
2. Calculate test coverage for the `app/` directory (excluding test code).
3. Output the results to the console.
4. Write detailed logs, including test output and coverage report, to `logs/test_run.log`.

## Checking Coverage Logs

After running `auto_test.py`, check the coverage results in `logs/test_run.log`. This file contains:
- The output from running the tests.
- A coverage report showing which lines of code in `app/` were executed during testing.

The coverage report indicates the percentage of code covered by tests, helping identify areas that may need additional testing.