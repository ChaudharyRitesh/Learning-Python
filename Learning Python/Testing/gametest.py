import unittest
import main

class TestGame(unittest.TestCase):
    def test_input(self):
        result = main.run_guess(3, 4)
        self.assertTrue(result)

    def test_input_incorrect(self):
        result = main.run_guess(5, 6)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()