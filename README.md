# Test additions and auto-runner

## Overview ✅
This workspace received the following generated files to improve test coverage and automation:

- `tests/test_discount.py` — unit tests for `app/discount.py`
- `tests/test_errors.py` — unit tests for `app/errors.py`
- `tests/test_permissions.py` — unit tests for `app/permissions.py`
- `tests/test_utils.py` — unit tests for `app/utils.py`
- `report.json` — list of previously untested modules and their test file mappings
- `auto_test.py` — test discovery + coverage runner that writes results to `logs/test_run.log`
- `logs/` — created by `auto_test.py` when you run it (contains `test_run.log`)

---

## How it works (quick) 💡
- `auto_test.py` runs `pytest` over the `tests/` directory.
- It then runs `coverage` limited to the `app/` package (excludes `tests/`) and writes a coverage report.
- All console output is saved to `logs/test_run.log`.

---

## Check coverage logs 🔍
Open `logs/test_run.log` after running `auto_test.py` to see:
- `pytest` output and failures
- `coverage` summary restricted to `app/` (tests are excluded)

---

## Run the automated test + coverage script 🔧
From the project root run:

```
python auto_test.py
```

Notes:
- Requires `pytest` and `coverage` to be installed in the environment.
- The script returns a non-zero exit code when tests or coverage execution fail; see `logs/test_run.log` for details.

---

If you want, I can run the test suite for you and open the log next."