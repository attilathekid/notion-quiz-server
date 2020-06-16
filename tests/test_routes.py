import unittest
import requests


class DoThePagesReturnStuff(unittest.TestCase):

    def test_index(self):
        r = requests.get(f'http://127.0.0.1:5000/')
        self.assertEqual(200, r.status_code, f'Request to index unsuccessful, code: {r.status_code}')

    def test_make_quiz(self):
        r = requests.get(f'http://127.0.0.1:5000/make_quiz')
        self.assertEqual(200, r.status_code, f'Request to make_quiz unsuccessful, code: {r.status_code}')


if __name__ == '__main__':
    unittest.main()
