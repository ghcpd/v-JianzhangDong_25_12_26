# Auto-generated Test Files & Runner ✅

## Overview
This project includes newly generated test files and helper files to improve test coverage for modules that previously had no direct tests.

**Generated files:**

- `tests/test_discount.py` 🔧 — Tests for `app.discount.apply_discount`.
- `tests/test_errors.py` 🔧 — Tests for the error classes in `app.errors`.
- `tests/test_permissions.py` 🔧 — Tests for `app.permissions.has_permission`.
- `tests/test_utils.py` 🔧 — Tests for `app.utils` (`normalize_email`, `utc_now_iso`).
- `report.json` 📋 — Machine readable list of the untested modules and their test file mappings.
- `auto_test.py` ⚙️ — Script that runs tests with `pytest` and measures coverage (for `app/` only), writing results to `logs/test_run.log`.

---

## How coverage is measured 📊
- The `auto_test.py` script uses `coverage` to measure coverage for the main source package `app/` only (`--source=app`).
- The `tests/` directory is not included in the coverage source (so tests do not inflate the measured coverage).
- The textual coverage report is written to `logs/test_run.log`.

---

## How to run the tests and view coverage 💡

1. Install test dependencies (if not already installed):

```bash
python -m pip install --upgrade pip
python -m pip install pytest coverage
```

2. Run the auto test runner:

```bash
python auto_test.py
```

3. Open the log to see the coverage report:

```bash
cat logs/test_run.log
# (or open in your editor on Windows)
```

---

## Notes & Tips ⚠️
- `auto_test.py` exits with the `pytest` return code so it integrates with CI pipelines.
- If `coverage` is not installed, the script will fail; install it using `pip install coverage`.

If you want any additional assertions, CI integration, or HTML coverage output, tell me which you prefer and I can add it. ✨
