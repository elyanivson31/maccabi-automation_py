# How to Create Tests for VS Code Discovery

## 📋 Pytest Naming Conventions

For VS Code (and pytest) to automatically discover your tests, follow these rules:

### ✅ File Naming

Your test files **must** match one of these patterns:

```
test_*.py          ← Recommended (e.g., test_login.py)
*_test.py          ← Alternative (e.g., login_test.py)
```

**Examples:**
- ✅ `test_open_new_appointment.py`
- ✅ `test_get_earlier_appointment.py`
- ✅ `test_data_loader.py`
- ✅ `login_test.py`
- ❌ `get_earlier_appointment.py` (missing `test_` prefix)
- ❌ `my_tests.py` (doesn't match pattern)

### ✅ Function Naming

Your test functions **must** start with `test_`:

```python
def test_something(driver: WebDriver):  ← Correct
    # test code here

def test_login():  ← Correct
    # test code here

def get_earlier_appointment(driver: WebDriver):  ← Won't be discovered!
    # test code here
```

---

## 🆕 Creating a New Test - Step by Step

### Example 1: Simple Test

```python
# File: tests/test_login.py

from infra.data_loader import DataLoader

def test_login_with_valid_credentials(driver):
    """Test that user can login with valid credentials."""
    loader = DataLoader()
    contact = loader.get_contact_by_name("yaniv")

    # Your test logic here
    assert contact["username"] is not None
```

### Example 2: Test with Setup

```python
# File: tests/test_appointment_booking.py

import pytest
from infra.data_loader import DataLoader
from flows.web_flow import WebFlow

def test_book_appointment(driver):
    """Test booking an appointment."""
    # Arrange
    data_loader = DataLoader()
    contact = data_loader.get_contact_by_name("yaniv_marina")
    web_flow = WebFlow(driver)

    # Act
    web_flow.login_flow().login_to_portal(contact)
    web_flow.main_flow().start_new_appointment()

    # Assert
    # Your assertions here
```

### Example 3: Multiple Tests in One File

```python
# File: tests/test_user_management.py

def test_create_user(driver):
    """Test user creation."""
    # test code
    pass

def test_delete_user(driver):
    """Test user deletion."""
    # test code
    pass

def test_update_user_profile(driver):
    """Test updating user profile."""
    # test code
    pass
```

---

## 📁 File Structure

Your tests should be in the `tests/` folder:

```
maccabi-automation_py/
├── tests/
│   ├── __init__.py                  ← Required for package
│   ├── test_open_new_appointment.py ✅
│   ├── test_get_earlier_appointment.py  ✅
│   ├── test_data_loader.py          ✅
│   └── test_your_new_test.py        ✅
├── infra/
├── flows/
└── ...
```

---

## 🔍 Verify Your Test is Discoverable

After creating a test file, verify pytest can find it:

```bash
# See all tests
python -m pytest --collect-only tests/

# See tests in specific file
python -m pytest --collect-only tests/test_your_new_test.py
```

You should see:
```
<Module test_your_new_test.py>
  <Function test_your_function>
```

---

## 🎯 Quick Checklist for New Tests

Before you create a test, make sure:

- [ ] File is in `tests/` folder
- [ ] File name starts with `test_` (e.g., `test_login.py`)
- [ ] Function name starts with `test_` (e.g., `def test_login():`)
- [ ] Function has proper parameters (e.g., `driver` fixture if needed)
- [ ] `tests/__init__.py` exists (already created)

---

## 🚀 See Your Test in VS Code

After creating a properly named test:

1. **Save the file**
2. **Open Testing Panel** (flask icon in sidebar)
3. **Click Refresh** if test doesn't appear automatically
4. **Run your test** by clicking the ▶️ play button

---

## 💡 Naming Tips

### Good Test Names (Descriptive)

```python
def test_login_with_valid_credentials():
def test_login_with_invalid_password():
def test_booking_appointment_before_threshold():
def test_user_can_view_appointment_history():
```

### Less Ideal (Too Generic)

```python
def test_1():
def test_case():
def test_something():
```

**Tip**: Test names should describe **what** you're testing and **what** the expected outcome is.

---

## 📖 Common Patterns

### Pattern 1: Arrange-Act-Assert

```python
def test_user_login(driver):
    # Arrange - Set up test data
    data_loader = DataLoader()
    contact = data_loader.get_contact_by_name("yaniv")

    # Act - Perform the action
    web_flow = WebFlow(driver)
    web_flow.login_flow().login_to_portal(contact)

    # Assert - Verify the outcome
    assert web_flow.main_flow().is_logged_in()
```

### Pattern 2: Using Fixtures

```python
@pytest.fixture
def logged_in_user(driver):
    """Fixture that logs in a user before the test."""
    data_loader = DataLoader()
    contact = data_loader.get_contact_by_name("yaniv")
    web_flow = WebFlow(driver)
    web_flow.login_flow().login_to_portal(contact)
    return web_flow

def test_start_appointment(logged_in_user):
    """Test starting an appointment (user already logged in)."""
    web_flow = logged_in_user
    web_flow.main_flow().start_new_appointment()
    # assertions here
```

---

## 🎓 Summary

**To create a test that VS Code can find:**

1. Create file: `tests/test_<feature_name>.py`
2. Write function: `def test_<what_you_are_testing>():`
3. Save file
4. Refresh VS Code Testing panel
5. Run test by clicking ▶️

**That's it!** Follow the naming conventions and VS Code will automatically discover all your tests. 🎉
