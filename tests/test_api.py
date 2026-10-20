import unittest

from app import app


class HealthTests(unittest.TestCase):
    def test_health(self):
        client = app.test_client()

        response = client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "ok"})