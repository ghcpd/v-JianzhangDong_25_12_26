# Test Suite Documentation

## Overview

This document describes the auto-generated test files, test coverage reports, and testing infrastructure for this Python project. The testing framework ensures comprehensive coverage of all modules in the application.

## Generated Files

### 1. Test Files (in `tests/` directory)

Four new test files were generated for previously untested modules:

#### **test_discount.py**
- **Module**: `app/discount.py`
- **Purpose**: Tests the discount calculation functionality
- **Coverage**:
  - VIP user discount (20% off)
  - Staff user discount (50% off)
  - Regular user (no discount)
  - Edge cases (zero price, large prices, unknown user levels)
- **Test Count**: 8 tests

#### **test_errors.py**
- **Module**: `app/errors.py`
- **Purpose**: Tests custom exception classes and error hierarchy
- **Coverage**:
  - AppError base class
  - AuthError exception
  - ValidationError exception
  - RepositoryError exception
  - Exception raising and catching
  - Error messages
- **Test Count**: 14 tests

#### **test_permissions.py**
- **Module**: `app/permissions.py`
- **Purpose**: Tests role-based access control (RBAC)
- **Coverage**:
  - Admin role permissions
  - User role permissions
  - Guest role permissions
  - Unknown roles
  - Unknown actions
  - Case sensitivity handling
- **Test Count**: 12 tests

#### **test_utils.py**
- **Module**: `app/utils.py`
- **Purpose**: Tests utility functions
- **Coverage**:
  - `utc_now_iso()`: ISO format timestamp generation
  - `normalize_email()`: Email normalization (lowercasing, whitespace stripping)
  - Mocking and edge cases
  - Special character handling
- **Test Count**: 15 tests

### 2. report.json

**Location**: Root directory (`report.json`)

**Purpose**: Catalogs all untested modules and their corresponding test files.

**Structure**:
```json
{
  "problems": [
    {
      "id": "1",
      "module_name": "discount",
      "file": "discount.py",
      "test_file": "test_discount.py"
    },
    ...
  ]
}
```

**Content**: Lists 4 previously untested modules:
- discount (app/discount.py)
- errors (app/errors.py)
- permissions (app/permissions.py)
- utils (app/utils.py)

### 3. auto_test.py

**Location**: Root directory (`auto_test.py`)

**Purpose**: Automated test runner with coverage analysis

**Features**:
- Discovers all test files in the `tests/` directory
- Runs tests using pytest framework
- Measures code coverage using coverage.py
- **Coverage includes only the `app/` directory** (excluding tests/)
- Generates both terminal and HTML coverage reports
- Writes comprehensive log to `logs/test_run.log`
- Creates `logs/` directory automatically if not present

**How to Run**:

```bash
python auto_test.py
```

**Requirements**:
The script requires the following packages to be installed:
```bash
pip install pytest pytest-cov coverage
```

**Output**:
- **Console Output**: Test results with coverage summary
- **Log File**: `logs/test_run.log` - Contains full test output and coverage details
- **HTML Report**: `htmlcov/index.html` - Interactive coverage report

## How to Check Coverage Logs

### View Log File
```bash
# Windows (PowerShell)
Get-Content logs\test_run.log

# Windows (Command Prompt)
type logs\test_run.log

# Linux/macOS
cat logs/test_run.log
```

### View HTML Coverage Report
After running `auto_test.py`, open the HTML report:
```bash
# Windows
start htmlcov\index.html

# Linux/macOS
open htmlcov/index.html
# or
xdg-open htmlcov/index.html
```

The HTML report shows:
- Overall coverage percentage
- Per-module coverage breakdown
- Line-by-line coverage details
- Missing coverage highlighted

## Test Statistics

### Total Test Files: 12
- **Existing Tests**: 8 files
- **New Tests**: 4 files

### Total Test Cases
- test_auth.py: ~8 tests (pre-existing)
- test_config.py: ~8 tests (pre-existing)
- test_logger.py: ~8 tests (pre-existing)
- test_order_service.py: ~10 tests (pre-existing)
- test_pricing.py: ~10 tests (pre-existing)
- test_repository.py: ~12 tests (pre-existing)
- test_user_service.py: ~10 tests (pre-existing)
- test_validators.py: ~6 tests (pre-existing)
- **test_discount.py: 8 tests (NEW)**
- **test_errors.py: 14 tests (NEW)**
- **test_permissions.py: 12 tests (NEW)**
- **test_utils.py: 15 tests (NEW)**

**Total New Tests**: 49 tests across 4 modules

## Project Structure

```
project-root/
├── app/                          # Source code
│   ├── __init__.py
│   ├── auth.py
│   ├── config.py
│   ├── discount.py              # [NEWLY TESTED]
│   ├── errors.py                # [NEWLY TESTED]
│   ├── logger.py
│   ├── order_service.py
│   ├── permissions.py           # [NEWLY TESTED]
│   ├── pricing.py
│   ├── repository.py
│   ├── user_service.py
│   ├── utils.py                 # [NEWLY TESTED]
│   └── validators.py
├── tests/                        # Test suite
│   ├── __init__.py
│   ├── test_auth.py
│   ├── test_config.py
│   ├── test_logger.py
│   ├── test_order_service.py
│   ├── test_pricing.py
│   ├── test_repository.py
│   ├── test_user_service.py
│   ├── test_validators.py
│   ├── test_discount.py         # [NEW]
│   ├── test_errors.py           # [NEW]
│   ├── test_permissions.py      # [NEW]
│   └── test_utils.py            # [NEW]
├── logs/                         # Auto-created by auto_test.py
│   └── test_run.log             # Test execution log
├── htmlcov/                      # Auto-created by auto_test.py
│   ├── index.html               # Coverage report
│   └── ...
├── auto_test.py                 # Test automation script [NEW]
├── report.json                  # Untested modules report [NEW]
└── README.md                    # This file [NEW]
```

## Workflow

### 1. Run Tests and Generate Coverage

```bash
python auto_test.py
```

### 2. Check Results

View the log file:
```bash
Get-Content logs\test_run.log  # PowerShell
```

View interactive HTML report:
```bash
start htmlcov\index.html  # PowerShell
```

### 3. Analyze Coverage

The coverage report shows:
- **% Covered**: Percentage of code lines covered by tests
- **Missing**: Line numbers not covered by tests
- **Excluded**: Lines excluded from coverage (e.g., comments, docstrings)

## Testing Best Practices Implemented

1. **Comprehensive Coverage**: All modules now have corresponding test files
2. **Descriptive Test Names**: Test methods clearly describe what they test
3. **Edge Case Testing**: Tests include boundary conditions and special cases
4. **Isolation**: Tests use mocking where appropriate (e.g., `test_utils.py`)
5. **Clear Assertions**: Each test verifies specific behavior
6. **Error Testing**: Exception classes and error conditions are tested
7. **Parameterized Testing**: Multiple scenarios tested for each function

## Troubleshooting

### pytest not found
```bash
pip install pytest pytest-cov coverage
```

### Coverage showing 0%
- Ensure tests are properly importing from `app/` modules
- Check that `app/` directory is in Python path
- Verify test files follow naming convention `test_*.py`

### Logs directory not created
- The script creates it automatically, but ensure you have write permissions
- Check your current working directory is the project root

### HTML report not opening
- HTML report is generated in `htmlcov/index.html`
- Open manually with your browser if automated opening fails

## Next Steps

1. Run `auto_test.py` to generate baseline coverage
2. Review coverage report to identify gaps
3. Improve coverage by:
   - Adding more test cases for edge scenarios
   - Testing error conditions and exceptions
   - Adding integration tests for module interactions
4. Monitor coverage trends over time

## Contact & Support

For questions about:
- **Test Structure**: Review specific test files in `tests/` directory
- **Coverage Metrics**: Check `logs/test_run.log` and `htmlcov/index.html`
- **Running Tests**: Execute `python auto_test.py` from project root

---

**Generated**: December 26, 2025  
**Test Framework**: unittest + pytest  
**Coverage Tool**: coverage.py  
**Python Version**: 3.6+
