"""
Encryption/Decryption utility for sensitive test data files.
Uses Fernet symmetric encryption with a key from environment variables.
"""
import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class CryptoUtils:
    """Handles encryption and decryption of sensitive data files."""

    ENCRYPTED_FILE = "test_data.json.enc"
    DECRYPTED_FILE = "test_data.json"

    @staticmethod
    def get_encryption_key():
        """
        Gets the encryption key from environment variable.
        Raises ValueError if not found.
        """
        key = os.getenv("TEST_DATA_ENCRYPTION_KEY")
        if not key:
            raise ValueError(
                "TEST_DATA_ENCRYPTION_KEY environment variable not set.\n"
                "Please set it with your encryption key to decrypt test data.\n"
                "If you're setting up for the first time, run: python setup_encryption.py"
            )
        return key

    @staticmethod
    def derive_key_from_password(password: str) -> bytes:
        """
        Derives a Fernet-compatible key from a password using PBKDF2.
        """
        # Use a fixed salt for derivation (in production, use a random salt stored separately)
        salt = b'maccabi-automation-salt-2026'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key

    @staticmethod
    def encrypt_file(input_file: str, output_file: str, password: str):
        """
        Encrypts a file using the provided password.
        """
        key = CryptoUtils.derive_key_from_password(password)
        fernet = Fernet(key)

        with open(input_file, 'rb') as f:
            data = f.read()

        encrypted_data = fernet.encrypt(data)

        with open(output_file, 'wb') as f:
            f.write(encrypted_data)

        print(f"✓ File encrypted: {input_file} -> {output_file}")

    @staticmethod
    def decrypt_file(input_file: str, output_file: str, password: str):
        """
        Decrypts a file using the provided password.
        """
        key = CryptoUtils.derive_key_from_password(password)
        fernet = Fernet(key)

        with open(input_file, 'rb') as f:
            encrypted_data = f.read()

        try:
            decrypted_data = fernet.decrypt(encrypted_data)
        except Exception as e:
            raise ValueError(f"Decryption failed. Invalid key or corrupted file: {e}")

        with open(output_file, 'wb') as f:
            f.write(decrypted_data)

        print(f"✓ File decrypted: {input_file} -> {output_file}")

    @staticmethod
    def ensure_decrypted_file_exists():
        """
        Ensures the decrypted test_data.json file exists.
        If not, attempts to decrypt from the encrypted version.
        """
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        decrypted_path = os.path.join(root_dir, CryptoUtils.DECRYPTED_FILE)
        encrypted_path = os.path.join(root_dir, CryptoUtils.ENCRYPTED_FILE)

        # If decrypted file already exists, no need to decrypt
        if os.path.exists(decrypted_path):
            return

        # Check if encrypted file exists
        if not os.path.exists(encrypted_path):
            raise FileNotFoundError(
                f"Neither {CryptoUtils.DECRYPTED_FILE} nor {CryptoUtils.ENCRYPTED_FILE} found.\n"
                "Please ensure the encrypted file exists in the repository."
            )

        # Decrypt the file
        password = CryptoUtils.get_encryption_key()
        CryptoUtils.decrypt_file(encrypted_path, decrypted_path, password)
        print(f"✓ Test data decrypted successfully to {CryptoUtils.DECRYPTED_FILE}")
