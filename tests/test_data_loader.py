"""
Unit tests for DataLoader with encryption.
Tests that DataLoader correctly loads and decrypts test data.
"""
import pytest
from infra.data_loader import DataLoader


class TestDataLoader:
    """Test suite for DataLoader with encryption support."""

    def test_data_loader_initialization(self):
        """Test that DataLoader can be initialized (triggers auto-decryption)."""
        loader = DataLoader()
        assert loader.data is not None
        assert isinstance(loader.data, dict)

    def test_get_contacts(self):
        """Test that contacts can be loaded from encrypted data."""
        loader = DataLoader()
        contacts = loader.data.get("contacts", [])

        assert len(contacts) > 0, "Should have at least one contact"
        assert isinstance(contacts, list)

    def test_get_contact_by_name(self):
        """Test getting a specific contact by name."""
        loader = DataLoader()

        # Test with known contact from test_data.json
        contact = loader.get_contact_by_name("yaniv")

        assert contact is not None
        assert contact["name"] == "yaniv"
        assert "username" in contact
        assert "password" in contact

    def test_get_contact_by_name_not_found(self):
        """Test that ValueError is raised for non-existent contact."""
        loader = DataLoader()

        with pytest.raises(ValueError, match="not found"):
            loader.get_contact_by_name("nonexistent_contact")

    def test_contact_structure(self):
        """Test that contact has expected structure."""
        loader = DataLoader()
        contact = loader.get_contact_by_name("yaniv")

        required_fields = ["name", "username", "password", "selectedPatient", "doctorName", "settings"]

        for field in required_fields:
            assert field in contact, f"Contact should have '{field}' field"

    def test_contact_settings(self):
        """Test that contact settings are properly loaded."""
        loader = DataLoader()
        contact = loader.get_contact_by_name("yaniv")

        settings = contact.get("settings", {})

        assert "appointmentThresholdDate" in settings
        assert "appointmentServiceName" in settings
        assert "appointmentDoctorCity" in settings
        assert "appointmentType" in settings

    def test_get_contact_setting(self):
        """Test getting a specific setting from a contact."""
        loader = DataLoader()

        # Test getting a known setting
        city = loader.get_contact_setting("yaniv", "appointmentDoctorCity")

        assert city is not None
        assert isinstance(city, str)

    def test_get_contact_setting_not_found(self):
        """Test that KeyError is raised for non-existent setting."""
        loader = DataLoader()

        with pytest.raises(KeyError, match="not found in settings"):
            loader.get_contact_setting("yaniv", "nonexistent_setting")

    def test_multiple_contacts(self):
        """Test that all contacts can be accessed."""
        loader = DataLoader()
        contacts = loader.data.get("contacts", [])

        # We know there are 3 contacts in test_data.json
        assert len(contacts) == 3

        contact_names = [c["name"] for c in contacts]
        assert "yaniv" in contact_names
        assert "yaniv_marina" in contact_names
        assert "yaniv_landov" in contact_names

    def test_data_integrity_after_decryption(self):
        """Test that decrypted data maintains integrity."""
        loader = DataLoader()

        # Get the same contact twice to ensure consistency
        contact1 = loader.get_contact_by_name("yaniv")
        contact2 = loader.get_contact_by_name("yaniv")

        assert contact1 == contact2
        assert contact1["username"] == contact2["username"]
        assert contact1["password"] == contact2["password"]
