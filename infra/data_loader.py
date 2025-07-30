import json
import os

class DataLoader:
    def __init__(self, file_path="test_data.json"):
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        full_path = os.path.join(root_dir, file_path)

        with open(full_path, encoding="utf-8") as f:
            self.data = json.load(f)

    def get_contact_by_name(self, name):
        """
        Returns the user dictionary matching the contact 'name'
        """
        contacts = self.data.get("contacts", [])
        for contact in contacts:
            if contact.get("name") == name:
                return contact
        raise ValueError(f"Contact with name '{name}' not found.")
    
    def get_logic_setting(self, key):
        """
        Returns a value from the 'logicSettings' section of the JSON by key.
        """
        logic_settings = self.data.get("logicSettings", {})
        if key in logic_settings:
            return logic_settings[key]
        raise KeyError(f"Key '{key}' not found in logicSettings.")

    def get_contact_setting(self, name, key):
        contact = self.get_contact_by_name(name)
        settings = contact.get("settings", {})
        if key in settings:
            return settings[key]
        raise KeyError(f"Key '{key}' not found in settings for contact '{name}'")