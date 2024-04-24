# tuneTest.py
import unittest

from src.tune import myrev


class MyTestCase(unittest.TestCase):
    def test_tune(self):
        # setup
        string1 = "hey you"
        expected = "uoy yeh"

        # execute
        actual = myrev(string1)

        # verify
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
