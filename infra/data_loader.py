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
