import unittest
from app import app


class IsItAlive(unittest.TestCase):

    def test_something(self):
        app.run()
        self.assert_(True)


if __name__ == '__main__':
    unittest.main()
