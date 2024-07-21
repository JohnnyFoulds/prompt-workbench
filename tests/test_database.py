# tests/test_database.py
import unittest
from backend.services.database import get_client, create_user, add_prompt, add_version, get_user_prompts, get_prompt_versions

class TestDatabaseService(unittest.TestCase):
    def test_get_client(self):
        client = get_client()
        self.assertIsNotNone(client)

if __name__ == '__main__':
    unittest.main()
