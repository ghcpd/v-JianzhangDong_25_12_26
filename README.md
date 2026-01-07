# Test additions and runner (auto-generated)

## What I added ✅

- `tests/test_discount.py` — unit tests for `app.discount.apply_discount`
- `tests/test_errors.py` — tests for error classes in `app.errors`
- `tests/test_permissions.py` — tests for `app.permissions.has_permission`
- `tests/test_utils.py` — tests for `app.utils` helpers
- `report.json` — machine-readable list of modules that were missing tests
- `auto_test.py` — convenience script that runs tests and produces a coverage report
- `logs/test_run.log` — generated after running `auto_test.py` (created at runtime)

## Purpose

These additions cover previously untested modules and provide a single script to run the full test + coverage workflow and save results to `logs/test_run.log`.

## How to run (local development) ⚙️

1. Install test/runtime dependencies (if you don't already have them):

   ```bash
   python -m pip install -U pytest coverage
   ```

2. Run the tests + coverage and write results to `logs/test_run.log`:

   ```bash
   python auto_test.py
   ```

   - The script runs `pytest` and, if available, `coverage`.
   - Coverage is measured for the `app/` package and the `tests/` directory is omitted from the coverage report.

3. To run only pytest:

   ```bash
   pytest -q
   ```

## Where to find results 📂

- Full test + coverage output: `logs/test_run.log`
- Machine-readable list of missing-test findings: `report.json`

## Notes & tips 💡

- The `auto_test.py` script is portable and uses your current Python interpreter (`sys.executable`).
- If `coverage` is not installed the script will still run `pytest` and record results, but the coverage section will be skipped.
