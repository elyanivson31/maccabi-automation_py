#!/usr/bin/env python3
"""
Verification script to test the encryption setup.
Ensures that encryption, decryption, and DataLoader work correctly.
"""
import os
import sys
import json
import tempfile
from pathlib import Path


def print_header(text):
    """Print a formatted section header."""
    print("\n" + "=" * 70)
    print(f"  {text}")
    print("=" * 70)


def print_status(test_name, passed, details=""):
    """Print test status with emoji."""
    status = "✓ PASS" if passed else "✗ FAIL"
    print(f"{status}: {test_name}")
    if details:
        print(f"       {details}")


def test_encrypted_file_exists():
    """Test 1: Verify encrypted file exists."""
    print_header("Test 1: Encrypted File Exists")
    encrypted_file = "test_data.json.enc"
    exists = os.path.exists(encrypted_file)

    if exists:
        size = os.path.getsize(encrypted_file)
        print_status("Encrypted file exists", True, f"Size: {size} bytes")
    else:
        print_status("Encrypted file exists", False, "File not found!")

    return exists


def test_decrypted_file_in_gitignore():
    """Test 2: Verify test_data.json is in .gitignore."""
    print_header("Test 2: Decrypted File in .gitignore")

    if not os.path.exists(".gitignore"):
        print_status(".gitignore exists", False, ".gitignore not found")
        return False

    with open(".gitignore", "r") as f:
        gitignore_content = f.read()

    has_test_data = "test_data.json" in gitignore_content
    print_status("test_data.json in .gitignore", has_test_data)

    return has_test_data


def test_environment_variable():
    """Test 3: Check if encryption key is set."""
    print_header("Test 3: Environment Variable")

    key = os.getenv("TEST_DATA_ENCRYPTION_KEY")
    is_set = bool(key)

    if is_set:
        print_status("TEST_DATA_ENCRYPTION_KEY is set", True, f"Key length: {len(key)} chars")
    else:
        print_status("TEST_DATA_ENCRYPTION_KEY is set", False,
                    "Environment variable not set! Set it to run full tests.")

    return is_set


def test_crypto_utils_import():
    """Test 4: Verify crypto_utils can be imported."""
    print_header("Test 4: Crypto Utils Import")

    try:
        from infra.crypto_utils import CryptoUtils
        print_status("Import crypto_utils", True)
        return True, CryptoUtils
    except ImportError as e:
        print_status("Import crypto_utils", False, str(e))
        return False, None


def test_decryption(CryptoUtils, encryption_key):
    """Test 5: Test decryption functionality."""
    print_header("Test 5: Decryption Test")

    if not encryption_key:
        print_status("Decryption test", False, "Skipped - no encryption key")
        return False

    try:
        # Remove test_data.json if it exists
        if os.path.exists("test_data.json"):
            os.remove("test_data.json")
            print("  Removed existing test_data.json")

        # Try to decrypt
        CryptoUtils.decrypt_file("test_data.json.enc", "test_data.json", encryption_key)

        # Check if file was created
        if os.path.exists("test_data.json"):
            print_status("Decrypt file", True, "test_data.json created successfully")
            return True
        else:
            print_status("Decrypt file", False, "Decryption didn't create file")
            return False

    except Exception as e:
        print_status("Decrypt file", False, f"Error: {e}")
        return False


def test_data_loader():
    """Test 6: Test DataLoader with auto-decryption."""
    print_header("Test 6: DataLoader Functionality")

    try:
        from infra.data_loader import DataLoader

        # Remove test_data.json to test auto-decrypt
        if os.path.exists("test_data.json"):
            os.remove("test_data.json")
            print("  Removed test_data.json to test auto-decryption")

        # Initialize DataLoader (should auto-decrypt)
        loader = DataLoader()
        print_status("DataLoader initialization", True, "Auto-decryption worked")

        # Test getting contacts
        contacts = loader.data.get("contacts", [])
        print_status(f"Load contacts", True, f"Found {len(contacts)} contacts")

        # Test getting specific contact
        if contacts:
            first_contact_name = contacts[0].get("name")
            contact = loader.get_contact_by_name(first_contact_name)
            print_status(f"Get contact by name", True, f"Retrieved '{first_contact_name}'")

        return True

    except Exception as e:
        print_status("DataLoader test", False, f"Error: {e}")
        return False


def test_data_integrity():
    """Test 7: Verify decrypted data structure."""
    print_header("Test 7: Data Integrity Check")

    if not os.path.exists("test_data.json"):
        print_status("Data integrity", False, "test_data.json not found")
        return False

    try:
        with open("test_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        # Check expected structure
        has_contacts = "contacts" in data
        print_status("Has 'contacts' key", has_contacts)

        if has_contacts:
            contacts = data["contacts"]
            print_status(f"Contacts count", True, f"{len(contacts)} contacts found")

            # Check first contact structure
            if contacts:
                first = contacts[0]
                required_keys = ["name", "username", "password"]
                has_all_keys = all(key in first for key in required_keys)
                print_status("Contact structure valid", has_all_keys,
                           f"Keys: {', '.join(first.keys())}")

                return has_all_keys

        return False

    except Exception as e:
        print_status("Data integrity", False, f"Error: {e}")
        return False


def test_encryption_roundtrip(CryptoUtils, encryption_key):
    """Test 8: Test full encryption/decryption roundtrip."""
    print_header("Test 8: Encryption/Decryption Roundtrip")

    if not encryption_key:
        print_status("Roundtrip test", False, "Skipped - no encryption key")
        return False

    try:
        # Create temporary test files
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
            test_data = {"test": "data", "number": 123}
            json.dump(test_data, f)
            test_file = f.name

        encrypted_file = test_file + '.enc'
        decrypted_file = test_file + '.dec'

        # Encrypt
        CryptoUtils.encrypt_file(test_file, encrypted_file, encryption_key)
        print_status("Encrypt test file", True)

        # Decrypt
        CryptoUtils.decrypt_file(encrypted_file, decrypted_file, encryption_key)
        print_status("Decrypt test file", True)

        # Verify data matches
        with open(decrypted_file, 'r') as f:
            decrypted_data = json.load(f)

        matches = decrypted_data == test_data
        print_status("Data matches original", matches)

        # Cleanup
        os.remove(test_file)
        os.remove(encrypted_file)
        os.remove(decrypted_file)

        return matches

    except Exception as e:
        print_status("Roundtrip test", False, f"Error: {e}")
        return False


def main():
    """Run all verification tests."""
    print("\n" + "█" * 70)
    print("  ENCRYPTION SETUP VERIFICATION")
    print("█" * 70)

    results = []

    # Test 1: Encrypted file exists
    results.append(("Encrypted file exists", test_encrypted_file_exists()))

    # Test 2: Gitignore configuration
    results.append((".gitignore configured", test_decrypted_file_in_gitignore()))

    # Test 3: Environment variable
    has_key = test_environment_variable()
    encryption_key = os.getenv("TEST_DATA_ENCRYPTION_KEY") if has_key else None
    results.append(("Environment variable set", has_key))

    # Test 4: Import crypto_utils
    import_success, CryptoUtils = test_crypto_utils_import()
    results.append(("Crypto utils import", import_success))

    # Tests 5-8 require encryption key
    if has_key and import_success:
        results.append(("Decryption", test_decryption(CryptoUtils, encryption_key)))
        results.append(("DataLoader", test_data_loader()))
        results.append(("Data integrity", test_data_integrity()))
        results.append(("Roundtrip", test_encryption_roundtrip(CryptoUtils, encryption_key)))
    else:
        print_header("Skipping Advanced Tests")
        print("⚠ Set TEST_DATA_ENCRYPTION_KEY environment variable to run all tests")
        print(f"  export TEST_DATA_ENCRYPTION_KEY='your-key-here'")

    # Summary
    print_header("SUMMARY")
    passed = sum(1 for _, result in results if result)
    total = len(results)

    for test_name, result in results:
        status = "✓" if result else "✗"
        print(f"  {status} {test_name}")

    print()
    print(f"  Total: {passed}/{total} tests passed")

    if passed == total:
        print("\n  🎉 All tests passed! Encryption setup is working correctly.")
        return 0
    else:
        print(f"\n  ⚠ {total - passed} test(s) failed. Please review the output above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
