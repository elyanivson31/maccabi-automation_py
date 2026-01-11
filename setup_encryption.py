#!/usr/bin/env python3
"""
Setup script to encrypt test_data.json file.
Run this once to create the encrypted version that will be committed to git.
"""
import os
import sys
import secrets
from infra.crypto_utils import CryptoUtils


def generate_secure_key():
    """Generates a secure random key for encryption."""
    return secrets.token_urlsafe(32)


def main():
    print("=" * 60)
    print("Test Data Encryption Setup")
    print("=" * 60)
    print()

    # Check if test_data.json exists
    if not os.path.exists("test_data.json"):
        print("❌ Error: test_data.json not found!")
        print("   Make sure you're running this from the project root.")
        sys.exit(1)

    # Check if already encrypted
    if os.path.exists("test_data.json.enc"):
        response = input("⚠ test_data.json.enc already exists. Overwrite? (yes/no): ")
        if response.lower() != 'yes':
            print("Aborted.")
            sys.exit(0)

    print("This script will:")
    print("  1. Generate or use an encryption key")
    print("  2. Encrypt test_data.json -> test_data.json.enc")
    print("  3. Provide instructions for team setup")
    print()

    # Option to use existing or generate new key
    print("Choose an option:")
    print("  1. Generate a new encryption key")
    print("  2. Use an existing encryption key")
    choice = input("Enter choice (1 or 2): ").strip()

    if choice == "1":
        encryption_key = generate_secure_key()
        print()
        print("✓ Generated new encryption key")
    elif choice == "2":
        encryption_key = input("Enter your encryption key: ").strip()
        if not encryption_key:
            print("❌ Error: Key cannot be empty")
            sys.exit(1)
    else:
        print("❌ Invalid choice")
        sys.exit(1)

    # Encrypt the file
    print()
    print("Encrypting test_data.json...")
    try:
        CryptoUtils.encrypt_file("test_data.json", "test_data.json.enc", encryption_key)
    except Exception as e:
        print(f"❌ Encryption failed: {e}")
        sys.exit(1)

    # Success message and instructions
    print()
    print("=" * 60)
    print("✓ SUCCESS! test_data.json has been encrypted")
    print("=" * 60)
    print()
    print("IMPORTANT - Save this encryption key securely:")
    print("-" * 60)
    print(encryption_key)
    print("-" * 60)
    print()
    print("Next steps:")
    print("  1. Add test_data.json to .gitignore (if not already)")
    print("  2. Commit test_data.json.enc to git")
    print("  3. Share the encryption key securely with your team")
    print("     (via password manager, secure chat, etc.)")
    print()
    print("Team members should:")
    print("  1. Clone the repository")
    print("  2. Set environment variable:")
    print(f"     export TEST_DATA_ENCRYPTION_KEY='{encryption_key}'")
    print("  3. Add to ~/.bashrc or ~/.zshrc to persist")
    print()
    print("The file will auto-decrypt when the code runs!")
    print()


if __name__ == "__main__":
    main()
