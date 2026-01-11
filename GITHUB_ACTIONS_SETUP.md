# GitHub Actions Setup Guide

## Overview

This project uses GitHub Actions to automatically validate pull requests before they can be merged into `main`. The CI pipeline ensures:

✅ Encrypted test data file exists
✅ Decrypted file is properly ignored
✅ Encryption/decryption works correctly
✅ DataLoader can load encrypted data
✅ Code quality and syntax are valid

## Required: Set Up GitHub Secret

**CRITICAL**: You must add the encryption key as a GitHub Secret for the CI pipeline to work.

### Step-by-Step Instructions

#### 1. Get Your Encryption Key

Your encryption key is (save this securely):
```
l8_bfAxxwkxpqczvLLr4lLqhmpQMqEtZ39MBTebDrzo
```

#### 2. Add Secret to GitHub Repository

1. Go to your GitHub repository: `https://github.com/elyanivson31/maccabi-automation_py`

2. Click **Settings** (repository settings, not your profile)

3. In the left sidebar, click **Secrets and variables** → **Actions**

4. Click **New repository secret**

5. Add the secret:
   - **Name**: `TEST_DATA_ENCRYPTION_KEY`
   - **Value**: `l8_bfAxxwkxpqczvLLr4lLqhmpQMqEtZ39MBTebDrzo`

6. Click **Add secret**

#### 3. Verify Setup

After adding the secret:
1. Create or update a pull request to `main`
2. GitHub Actions will automatically run
3. Check the "Actions" tab to see the results

## CI Workflow Details

### Workflow File
`.github/workflows/pr-validation.yml`

### When It Runs
- On every pull request to `main`
- On every push to `main`

### Jobs

#### Job 1: Validate Encryption & Data Loading
- ✓ Checks encrypted file exists
- ✓ Verifies .gitignore configuration
- ✓ Ensures decrypted file is NOT committed
- ✓ Runs encryption verification tests (8 tests)
- ✓ Tests DataLoader with encrypted data

#### Job 2: Code Quality Checks
- ✓ Validates Python syntax
- ✓ Verifies project structure
- ✓ Checks required files exist

### What Happens on PR

When you create a pull request:

1. GitHub Actions automatically starts
2. Two jobs run in parallel:
   - Encryption validation
   - Code quality checks
3. Both jobs must pass ✓
4. If any job fails ✗, the PR cannot be merged
5. You'll see status checks on the PR page

### Viewing Results

1. Go to your PR on GitHub
2. Scroll down to see "Checks" section
3. Click on failed checks to see details
4. Fix any issues and push again (workflow re-runs automatically)

## Troubleshooting

### Error: "TEST_DATA_ENCRYPTION_KEY environment variable not set"

**Solution**: The GitHub Secret is not configured. Follow steps above to add it.

### Error: "test_data.json should not be committed to git"

**Solution**: Someone committed the decrypted file. Remove it:
```bash
git rm --cached test_data.json
git commit -m "Remove decrypted test_data.json"
git push
```

### Error: "test_data.json.enc not found"

**Solution**: The encrypted file is missing. Run:
```bash
python setup_encryption.py
git add test_data.json.enc
git commit -m "Add encrypted test data"
git push
```

### Workflow Not Running

**Check**:
1. Workflow file is in `.github/workflows/pr-validation.yml`
2. You're creating a PR to the `main` branch
3. GitHub Actions are enabled for your repository

## Branch Protection (Optional but Recommended)

To enforce that PRs can only be merged if CI passes:

1. Go to **Settings** → **Branches**
2. Click **Add rule** for `main` branch
3. Enable:
   - ✓ Require status checks to pass before merging
   - ✓ Select: "Validate Encryption & Data Loading"
   - ✓ Select: "Code Quality Checks"
4. Save changes

Now PRs to `main` cannot be merged unless all checks pass! 🎉

## Local Testing Before Pushing

Test locally before pushing to avoid CI failures:

```bash
# Set encryption key
export TEST_DATA_ENCRYPTION_KEY='l8_bfAxxwkxpqczvLLr4lLqhmpQMqEtZ39MBTebDrzo'

# Run verification
python verify_encryption.py

# Or use quick test
./quick_test.sh
```

## CI Pipeline Status Badge (Optional)

Add this to your README.md to show CI status:

```markdown
![CI Status](https://github.com/elyanivson31/maccabi-automation_py/workflows/PR%20Validation/badge.svg)
```

## Summary

✅ GitHub Actions runs automatically on every PR
✅ Validates encryption setup
✅ Tests data loading
✅ Checks code quality
✅ Prevents merging broken code

**Important**: Don't forget to add the `TEST_DATA_ENCRYPTION_KEY` secret to GitHub!
