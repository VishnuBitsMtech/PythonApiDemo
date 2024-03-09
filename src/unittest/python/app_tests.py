import unittest
import requests

class TestAPI(unittest.TestCase):
    BASE_URL = 'http://localhost:5000'

    def test_index(self):
        response = requests.get(f'{self.BASE_URL}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'Sample Api Project!')

    def test_api_endpoint(self):
        response = requests.get(f'{self.BASE_URL}/api')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'This is my API endpoint'})

if __name__ == '__main__':
    unittest.main()
