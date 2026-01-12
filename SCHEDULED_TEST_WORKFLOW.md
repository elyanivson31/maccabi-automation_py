# Scheduled Test Workflow - test_get_earlier_appointment

This document explains the GitHub Actions workflow that runs `test_get_earlier_appointment` automatically every 5 minutes until the test passes.

## Overview

The workflow `test-get-earlier-appointment-scheduled.yml` is configured to:
- Run every 5 minutes (minimum interval for GitHub Actions scheduled workflows)
- Continue running until the test passes (finds an available appointment)
- Install all necessary dependencies including Chrome and Selenium
- Use encrypted test data with the encryption key from GitHub Secrets
- Send Telegram notifications when an appointment is found

## How It Works

### Schedule
- **Frequency**: Every 5 minutes
- **Duration**: Runs indefinitely until manually disabled
- **Recommendation**: Disable after 24 hours (288 runs) if test hasn't passed

### Test Flow
1. Set up Python 3.11 environment
2. Install Chrome browser (stable version)
3. Install all Python dependencies from `requirements.txt`
4. Verify encrypted test data exists
5. Verify required secrets are configured
6. Run `test_get_earlier_appointment` with pytest
7. Report results and upload logs

### Success Condition
The test passes when:
- An appointment is found that meets the threshold date criteria
- The appointment is in the specified city
- A Telegram notification is successfully sent
- **The workflow automatically disables itself** to stop further scheduled runs

## Required GitHub Secrets

Configure these secrets in your repository:
**Settings → Secrets and variables → Actions → New repository secret**

1. **TEST_DATA_ENCRYPTION_KEY** (Required)
   - The encryption key for `test_data.json.enc`
   - Without this, the test cannot decrypt contact information

2. **TELEGRAM_BOT_TOKEN** (Optional but recommended)
   - Your Telegram bot token for sending notifications
   - Format: `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`

3. **TELEGRAM_CHANNEL_ID** (Optional but recommended)
   - The Telegram channel/chat ID to send notifications to
   - Format: `-1001234567890` or `@channel_name`

## How to Enable the Workflow

The workflow is automatically enabled when pushed to the repository. It will start running on its schedule.

### Manual Trigger
You can also trigger the workflow manually:
1. Go to **Actions** tab in GitHub
2. Select **"Test Get Earlier Appointment - Every 5 Minutes"**
3. Click **"Run workflow"** button
4. Select the branch and click **"Run workflow"**

## Auto-Disable When Test Passes

**The workflow automatically disables itself when the test passes!**

When an appointment is found:
1. Telegram notification is sent
2. Test passes (exits with code 0)
3. Workflow uses GitHub API to disable itself
4. No further scheduled runs will occur

You can re-enable it anytime from the Actions tab if needed.

## Manual Disable (Optional)

If you want to stop the workflow before it finds an appointment:

1. Go to **Actions** tab in your GitHub repository
2. Click on **"Test Get Earlier Appointment - Every 5 Minutes"** in the left sidebar
3. Click the **"..."** menu button (three dots) in the top right
4. Select **"Disable workflow"**

## Monitoring the Workflow

### View Run History
- Navigate to **Actions** → **"Test Get Earlier Appointment - Every 5 Minutes"**
- See all runs with their status (✅ Success / ❌ Failure)

### Check Logs
- Click on any workflow run
- Click on the job name to see detailed logs
- Download artifacts if available (test logs)

### Calculate Runtime
The workflow shows approximate runtime in the logs:
- **Run number** × 5 minutes = Total minutes
- Example: Run #288 = 288 × 5 = 1,440 minutes = 24 hours

## Test Results

### When Test Passes ✅
- Exit code: 0 (success)
- Message: "✅ TEST PASSED! Appointment found!"
- A Telegram notification is sent with appointment details
- **Workflow automatically disables itself** - no further runs will occur

### When Test Fails ❌
- Exit code: 1 (failure)
- Message: "❌ Test failed - no appointment found yet"
- Workflow will retry in 5 minutes
- Continues until test passes or workflow is disabled

## Troubleshooting

### Workflow Not Running
- Check if the workflow is enabled (Actions → workflow → enabled status)
- Verify the schedule syntax in the YAML file
- GitHub Actions schedules can have delays during high load

### Test Failures
1. **Encryption Key Error**
   - Verify `TEST_DATA_ENCRYPTION_KEY` secret is set correctly
   - Check secret value matches your local encryption key

2. **Chrome/Selenium Errors**
   - Chrome is installed automatically by the workflow
   - Check logs for specific Selenium errors
   - Headless mode is configured in `driver_factory.py`

3. **Telegram Notification Errors**
   - Test will still pass if appointment is found
   - Check `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHANNEL_ID` secrets
   - Verify bot has permission to post in the channel

### Log Artifacts
- Test logs are automatically uploaded after each run
- Retention: 7 days
- Download from the workflow run page

## Cost Considerations

GitHub Actions includes:
- **Free tier**: 2,000 minutes/month for public repos
- **Free tier**: 2,000 minutes/month for private repos (GitHub Free)

**This workflow usage**:
- Each run: ~5 minutes
- Runs per hour: 12
- Runs per day: 288
- **Total for 24 hours**: ~1,440 minutes

**Recommendation**: Monitor your Actions usage in Settings → Billing

## Alternative: Local Execution

If you prefer to run locally instead of GitHub Actions:

```bash
# Run once
pytest tests/test_get_earlier_appointment.py::test_get_earlier_appointment -v

# Run in a loop (Unix/Mac)
while true; do
  pytest tests/test_get_earlier_appointment.py::test_get_earlier_appointment -v
  if [ $? -eq 0 ]; then
    echo "Test passed! Exiting."
    break
  fi
  echo "Waiting 5 minutes..."
  sleep 300
done
```

## Security Notes

- Never commit `test_data.json` (unencrypted) to git
- Keep `.env` files local (in `.gitignore`)
- Use GitHub Secrets for all sensitive data
- Encrypted `test_data.json.enc` is safe to commit
- Review `SECURITY_SETUP.md` for more details

## Related Documentation

- [SECURITY_SETUP.md](SECURITY_SETUP.md) - Encryption setup
- [ENCRYPTION_WORKFLOW_README.md](ENCRYPTION_WORKFLOW_README.md) - Encryption workflow
- [GITHUB_ACTIONS_SETUP.md](GITHUB_ACTIONS_SETUP.md) - GitHub Actions setup
- [HOW_TO_CREATE_TESTS.md](HOW_TO_CREATE_TESTS.md) - Creating tests
