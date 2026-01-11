#!/usr/bin/env python3
"""
Helper script to update test data after making changes.
Run this after editing test_data.json to re-encrypt it.
"""
import os
import sys
from infra.crypto_utils import CryptoUtils


def main():
    print("=" * 60)
    print("Update Test Data Helper")
    print("=" * 60)
    print()

    # Check if test_data.json exists
    if not os.path.exists("test_data.json"):
        print("❌ Error: test_data.json not found!")
        print("   Please create or decrypt it first.")
        sys.exit(1)

    # Get encryption key from environment
    key = os.getenv("TEST_DATA_ENCRYPTION_KEY")
    if not key:
        print("❌ Error: TEST_DATA_ENCRYPTION_KEY not set!")
        print()
        print("Set it with:")
        print("  export TEST_DATA_ENCRYPTION_KEY='your-key-here'")
        sys.exit(1)

    print("✓ Found test_data.json")
    print("✓ Encryption key is set")
    print()

    # Encrypt
    try:
        CryptoUtils.encrypt_file("test_data.json", "test_data.json.enc", key)
        print()
        print("=" * 60)
        print("✓ SUCCESS! test_data.json.enc has been updated")
        print("=" * 60)
        print()
        print("Next steps:")
        print("  1. Review your changes:")
        print("     git diff test_data.json.enc")
        print()
        print("  2. Commit the encrypted file:")
        print("     git add test_data.json.enc")
        print("     git commit -m 'Update test data'")
        print()
        print("  3. Push to remote:")
        print("     git push")
        print()
        print("Note: test_data.json (decrypted) is NOT committed.")
        print("      Only test_data.json.enc is tracked by git.")
        print()
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
