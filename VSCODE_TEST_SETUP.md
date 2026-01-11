# VS Code Test Setup Guide

## The Issue
VS Code can't find tests because **pytest and dependencies aren't installed** in your Python environment.

---

## ✅ Solution: Install Dependencies

### Step 1: Install All Requirements
```bash
pip install -r requirements.txt
```

This installs:
- pytest (for running tests)
- selenium (required by conftest.py)
- All other project dependencies

### Step 2: Verify pytest is installed
```bash
python -m pytest --version
```

You should see: `pytest 8.4.1` or similar

### Step 3: Set Encryption Key
```bash
# Add to ~/.bashrc or ~/.zshrc for persistence
export TEST_DATA_ENCRYPTION_KEY='l8_bfAxxwkxpqczvLLr4lLqhmpQMqEtZ39MBTebDrzo'
```

### Step 4: Restart VS Code
**Important**: Close and reopen VS Code completely (not just reload window)

### Step 5: Discover Tests
1. Open VS Code
2. Click the **Testing** icon (flask/beaker) in the left sidebar
3. Click the **Refresh** button at the top of the Testing panel
4. You should now see your tests!

---

## 🔍 Verify Test Discovery Works

Run this command to verify pytest can find your tests:

```bash
export TEST_DATA_ENCRYPTION_KEY='l8_bfAxxwkxpqczvLLr4lLqhmpQMqEtZ39MBTebDrzo'
python -m pytest --collect-only tests/
```

Expected output:
```
<Module test_data_loader.py>
  <Function test_data_loader_initialization>
  <Function test_get_contacts>
  ...
<Module test_open_new_appointment.py>
  <Function test_open_new_appointment>
```

---

## 🐍 Check Python Interpreter in VS Code

Make sure VS Code is using the correct Python interpreter:

1. Click bottom-left corner where it shows Python version
2. Select the interpreter where you installed the requirements
3. If using a virtual environment, select that environment

---

## 📋 Quick Checklist

Before tests will show in VS Code, verify:

- [ ] `pip install -r requirements.txt` completed successfully
- [ ] `python -m pytest --version` shows pytest is installed
- [ ] `export TEST_DATA_ENCRYPTION_KEY='...'` is set (add to shell config)
- [ ] VS Code is completely restarted (not just reloaded)
- [ ] Correct Python interpreter is selected in VS Code
- [ ] Testing panel is open (click flask icon in sidebar)
- [ ] Clicked refresh button in Testing panel

---

## 🐛 Still Not Working?

### Check VS Code Output Logs

1. **View** → **Output**
2. Select **"Python Test Log"** from the dropdown
3. Look for error messages

Common errors:
- `ModuleNotFoundError: No module named 'selenium'` → Run `pip install -r requirements.txt`
- `ModuleNotFoundError: No module named 'pytest'` → Run `pip install pytest`
- `TEST_DATA_ENCRYPTION_KEY not set` → Set the environment variable

### Manual Test Discovery

Try running:
```bash
# From VS Code terminal
python -m pytest tests/test_data_loader.py -v
```

If this works but VS Code doesn't show tests, try:
1. **Command Palette** (`Cmd/Ctrl + Shift + P`)
2. Run: **"Python: Configure Tests"**
3. Select **"pytest"**
4. Select **"tests"** as the directory

---

## ✨ Once Working

You'll see tests in the Testing panel:

```
📁 tests
  📄 test_data_loader.py
    ▶️ test_data_loader_initialization
    ▶️ test_get_contacts
    ▶️ test_get_contact_by_name
    ▶️ ...
  📄 test_open_new_appointment.py
    ▶️ test_open_new_appointment
```

Click the ▶️ button to run any test!

---

## 🎯 Quick Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Set encryption key (add to ~/.bashrc for persistence)
export TEST_DATA_ENCRYPTION_KEY='l8_bfAxxwkxpqczvLLr4lLqhmpQMqEtZ39MBTebDrzo'

# Verify pytest works
python -m pytest --collect-only tests/

# Run all tests
python -m pytest tests/ -v

# Run specific test
python -m pytest tests/test_data_loader.py -v
```
