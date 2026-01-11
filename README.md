# Maccabi Automation

Automated appointment booking system for Maccabi healthcare services.

## 🔒 Security

This project uses **encrypted test data** to protect sensitive credentials. See [ENCRYPTION_WORKFLOW_README.md](ENCRYPTION_WORKFLOW_README.md) for quick setup.

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/elyanivson31/maccabi-automation_py.git
cd maccabi-automation_py
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Encryption Key
```bash
# Contact team lead for the encryption key
export TEST_DATA_ENCRYPTION_KEY='your-encryption-key-here'
```

### 4. Run Tests
```bash
pytest tests/ -v
```

## 📚 Documentation

- **[ENCRYPTION_WORKFLOW_README.md](ENCRYPTION_WORKFLOW_README.md)** - Quick reference for encryption workflow
- **[SECURITY_SETUP.md](SECURITY_SETUP.md)** - Complete encryption documentation
- **[GITHUB_ACTIONS_SETUP.md](GITHUB_ACTIONS_SETUP.md)** - CI/CD pipeline setup
- **[VSCODE_TEST_SETUP.md](VSCODE_TEST_SETUP.md)** - VS Code test discovery setup
- **[HOW_TO_CREATE_TESTS.md](HOW_TO_CREATE_TESTS.md)** - Guide for creating new tests

## 🧪 Testing

### Run All Tests
```bash
pytest tests/
```

### Run Specific Test
```bash
pytest tests/test_open_new_appointment.py -v
```

### Run in VS Code
1. Open Testing panel (flask icon)
2. Click refresh to discover tests
3. Click ▶️ to run any test

## 🔐 Encryption Workflow

Test data is encrypted for security. Quick workflow:

```bash
# 1. Edit test data
nano test_data.json

# 2. Re-encrypt
python update_test_data.py

# 3. Commit encrypted version
git add test_data.json.enc
git commit -m "Update test data"
git push
```

See [ENCRYPTION_WORKFLOW_README.md](ENCRYPTION_WORKFLOW_README.md) for details.

## 🤖 CI/CD

GitHub Actions automatically run on every PR to `main`:
- ✅ Encryption validation
- ✅ Data loading tests
- ✅ Code quality checks

See [GITHUB_ACTIONS_SETUP.md](GITHUB_ACTIONS_SETUP.md) for setup instructions.

## 📁 Project Structure

```
maccabi-automation_py/
├── tests/              # Test files
├── infra/              # Infrastructure (data loading, crypto, drivers)
├── flows/              # User flow implementations
├── api/                # API integrations
├── utils/              # Utility functions
└── *.md               # Documentation
```

## 🛠️ Development

### Prerequisites
- Python 3.11+
- Chrome/Chromium browser
- pytest

### Setting Up Development Environment
```bash
# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install dependencies
pip install -r requirements.txt

# Set encryption key
export TEST_DATA_ENCRYPTION_KEY='your-key-here'
```

## 📝 License

Private repository - All rights reserved.
