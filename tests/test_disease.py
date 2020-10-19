import unittest
from app import app


class BasicTestCase(unittest.TestCase):

    def test_search_disease(self):
        test = app.test_client(self)
        response = test.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_other(self):
        test = app.test_client(self)
        response = test.post('/', data={"name": "Wolman", "days": 14})
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
