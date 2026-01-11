# Test Data Encryption - Quick Reference Guide

> **TL;DR**: Your test data is encrypted. Set the encryption key as an environment variable, and everything works automatically.

---

## 🔑 Encryption Key

**IMPORTANT**: Save this encryption key securely!

```
l8_bfAxxwkxpqczvLLr4lLqhmpQMqEtZ39MBTebDrzo
```

Store it in a password manager and share it securely with your team.

---

## 🚀 Quick Setup (First Time)

### 1. Set the Encryption Key

**Option A - Temporary (for current session):**
```bash
export TEST_DATA_ENCRYPTION_KEY='l8_bfAxxwkxpqczvLLr4lLqhmpQMqEtZ39MBTebDrzo'
```

**Option B - Permanent (recommended):**

For **bash** (`~/.bashrc` or `~/.bash_profile`):
```bash
echo "export TEST_DATA_ENCRYPTION_KEY='l8_bfAxxwkxpqczvLLr4lLqhmpQMqEtZ39MBTebDrzo'" >> ~/.bashrc
source ~/.bashrc
```

For **zsh** (`~/.zshrc`):
```bash
echo "export TEST_DATA_ENCRYPTION_KEY='l8_bfAxxwkxpqczvLLr4lLqhmpQMqEtZ39MBTebDrzo'" >> ~/.zshrc
source ~/.zshrc
```

### 2. Install Dependencies
```bash
pip install cryptography
```

### 3. Run Your Tests
```bash
pytest tests/
```

**That's it!** The test data will auto-decrypt when needed. ✨

---

## 📝 How to Update Test Data

When you need to add or modify test data:

### Step 1: Edit the decrypted file
```bash
nano test_data.json
# or use your favorite editor
```

### Step 2: Re-encrypt it
```bash
python3 update_test_data.py
```

### Step 3: Commit and push
```bash
git add test_data.json.enc
git commit -m "Update test data - added new contact"
git push
```

**Important**:
- ✅ Commit `test_data.json.enc` (encrypted)
- ❌ DON'T commit `test_data.json` (decrypted - it's in .gitignore)

---

## 🧪 Verify Everything Works

Run the verification script anytime:

```bash
./quick_test.sh
```

Or run the comprehensive tests:

```bash
python3 verify_encryption.py
```

---

## 👥 Team Member Setup

When a team member clones the repo:

1. **Get the encryption key** (from password manager or team lead)
2. **Set it as environment variable** (see Quick Setup above)
3. **Install dependencies**: `pip install cryptography`
4. **Run tests** - data auto-decrypts!

---

## 🤖 GitHub Actions CI/CD

**Setup Required**: Add the encryption key as a GitHub Secret

1. Go to: `https://github.com/YOUR_USERNAME/YOUR_REPO/settings/secrets/actions`
2. Click "New repository secret"
3. Name: `TEST_DATA_ENCRYPTION_KEY`
4. Value: `l8_bfAxxwkxpqczvLLr4lLqhmpQMqEtZ39MBTebDrzo`
5. Save

**What it does**:
- ✓ Runs on every PR to `main`
- ✓ Validates encryption setup
- ✓ Tests data loading
- ✓ Checks code quality
- ✓ Prevents merging if tests fail

See `GITHUB_ACTIONS_SETUP.md` for details.

---

## 🗂️ File Overview

| File | Status | Purpose |
|------|--------|---------|
| `test_data.json` | ❌ NOT in git (local only) | Decrypted data for local testing |
| `test_data.json.enc` | ✅ In git | Encrypted data (safe to share) |
| `update_test_data.py` | Helper script | Re-encrypts after changes |
| `verify_encryption.py` | Test script | Verifies encryption works |
| `quick_test.sh` | Test script | Quick verification |

---

## 🔧 Troubleshooting

### Error: "TEST_DATA_ENCRYPTION_KEY environment variable not set"
**Fix**: Set the environment variable (see Quick Setup)

### Error: "Decryption failed. Invalid key"
**Fix**: You have the wrong encryption key. Get the correct one from your team.

### Error: "test_data.json.enc not found"
**Fix**: Pull the latest changes from git: `git pull`

### I modified test_data.json but tests still use old data
**Fix**:
```bash
rm test_data.json  # Delete old decrypted file
# Run tests again - will auto-decrypt fresh copy
```

### I accidentally committed test_data.json
**Fix**:
```bash
git rm --cached test_data.json
git commit -m "Remove decrypted test data"
git push
```

---

## 📚 Complete Documentation

- **Security Setup**: `SECURITY_SETUP.md` - Complete encryption documentation
- **GitHub Actions**: `GITHUB_ACTIONS_SETUP.md` - CI/CD pipeline details
- **This Guide**: Quick reference for daily workflow

---

## ⚡ Common Commands Cheat Sheet

```bash
# Set encryption key (add to ~/.bashrc for persistence)
export TEST_DATA_ENCRYPTION_KEY='l8_bfAxxwkxpqczvLLr4lLqhmpQMqEtZ39MBTebDrzo'

# Run tests (auto-decrypts data)
pytest tests/

# Verify encryption setup
./quick_test.sh

# Update test data workflow
nano test_data.json          # 1. Edit
python3 update_test_data.py  # 2. Re-encrypt
git add test_data.json.enc   # 3. Stage
git commit -m "Update data"  # 4. Commit
git push                     # 5. Push

# Force fresh decrypt (if needed)
rm test_data.json
pytest tests/  # Will auto-decrypt
```

---

## 🔐 Security Best Practices

✅ **DO**:
- Store the encryption key in a password manager
- Share the key through secure channels (encrypted chat, password manager)
- Add the key to your environment variables
- Commit `test_data.json.enc` to git
- Re-encrypt after modifying test data

❌ **DON'T**:
- Commit `test_data.json` (decrypted) to git
- Share the encryption key in plain text emails
- Hardcode the key in your code
- Forget to re-encrypt after changes

---

## 🆘 Need Help?

1. Check `SECURITY_SETUP.md` for detailed documentation
2. Run `python3 verify_encryption.py` to diagnose issues
3. Ask your team lead for the encryption key if you don't have it

---

**Remember**: The encryption happens automatically. You just need to set the key once, and everything else works seamlessly! 🎉
