# Security Setup - Test Data Encryption

## Overview

This project uses encrypted test data to protect sensitive credentials. The `test_data.json` file contains usernames and passwords that should never be committed in plain text to the repository.

## How It Works

1. **Encrypted File**: `test_data.json.enc` (committed to git) - encrypted version of test data
2. **Decrypted File**: `test_data.json` (in .gitignore) - automatically decrypted when code runs
3. **Encryption Key**: Stored as environment variable `TEST_DATA_ENCRYPTION_KEY`

## Initial Setup (First Time)

### For Project Maintainers - Encrypting for the First Time

If you're setting up encryption for the first time:

```bash
# Install required dependency
pip install cryptography

# Run the setup script
python setup_encryption.py
```

The script will:
1. Generate a secure encryption key (or use your existing one)
2. Encrypt `test_data.json` → `test_data.json.enc`
3. Display the key (save it securely!)

**Important**: Share the encryption key with your team through a secure channel (password manager, encrypted chat, etc.). Never commit the key to git!

## Team Member Setup

When you clone this repository for the first time:

### Step 1: Install Dependencies

```bash
pip install cryptography
```

### Step 2: Get the Encryption Key

Ask your team lead for the `TEST_DATA_ENCRYPTION_KEY`. This key is never stored in the repository for security reasons.

### Step 3: Set the Environment Variable

#### Option A: Temporary (for current session)
```bash
export TEST_DATA_ENCRYPTION_KEY='your-key-here'
```

#### Option B: Permanent (recommended)

Add to your shell configuration file:

**For bash** (`~/.bashrc` or `~/.bash_profile`):
```bash
echo "export TEST_DATA_ENCRYPTION_KEY='your-key-here'" >> ~/.bashrc
source ~/.bashrc
```

**For zsh** (`~/.zshrc`):
```bash
echo "export TEST_DATA_ENCRYPTION_KEY='your-key-here'" >> ~/.zshrc
source ~/.zshrc
```

#### Option C: Using .env file

1. Copy the example file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your key:
   ```
   TEST_DATA_ENCRYPTION_KEY=your-key-here
   ```

3. Load it before running tests (if using python-dotenv):
   ```python
   from dotenv import load_dotenv
   load_dotenv()
   ```

### Step 4: Verify Setup

Run your tests - the file will automatically decrypt:

```bash
pytest
```

On first run, you should see: `✓ Test data decrypted successfully to test_data.json`

## How Auto-Decryption Works

The `DataLoader` class automatically:
1. Checks if `test_data.json` exists
2. If not, decrypts `test_data.json.enc` using your environment variable
3. Loads the decrypted data

No manual decryption needed!

## Updating Test Data

To update the test data:

1. Modify the decrypted `test_data.json` file locally
2. Re-encrypt it:
   ```bash
   python setup_encryption.py
   ```
3. Commit the new `test_data.json.enc`
4. Delete the decrypted `test_data.json` locally (it will be regenerated from the encrypted version)

## Security Best Practices

✅ **DO**:
- Store the encryption key in a password manager
- Share the key through secure channels (encrypted chat, password manager sharing)
- Add encryption key to your environment variables
- Commit `test_data.json.enc` to git

❌ **DON'T**:
- Commit `test_data.json` to git (it's in .gitignore)
- Share the encryption key in plain text emails or chat
- Hardcode the key in your code
- Commit the `.env` file to git

## Troubleshooting

### Error: "TEST_DATA_ENCRYPTION_KEY environment variable not set"
**Solution**: Set the environment variable as described in Step 3 above.

### Error: "Decryption failed. Invalid key or corrupted file"
**Solution**: Your encryption key is incorrect. Verify you have the correct key from your team lead.

### Error: "Neither test_data.json nor test_data.json.enc found"
**Solution**: Make sure you've pulled the latest changes from git that include `test_data.json.enc`.

## Files Overview

- `test_data.json.enc` - Encrypted test data (committed to git) ✅
- `test_data.json` - Decrypted test data (auto-generated, in .gitignore) 🔒
- `infra/crypto_utils.py` - Encryption/decryption utilities
- `setup_encryption.py` - Script to encrypt test data
- `.env.example` - Example environment variables file
