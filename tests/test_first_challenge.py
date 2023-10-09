import unittest
from first_challenge import counter


class EasyTestCase(unittest.TestCase):
    def test_easy_input(self):
        return self.assertEqual(counter("Sara"), 4)

    def test_easy_input_two(self):
        return self.assertEqual(counter("Mehrdad"), 7)


class MediumTestCase(unittest.TestCase):
    def test_medium_input(self):
        with self.assertRaises(Exception):
            return self.assertEqual(counter("mina111"), 4)

    def test_medium_input_two(self):
        with self.assertRaises(Exception):
            return self.assertEqual(counter(0), 4)


class HardTestCase(unittest.TestCase):
    def test_hard_input(self):
        with self.assertRaises(Exception):
            return self.assertEqual(counter(None), 4)

    def test_hard_input_two(self):
        with self.assertRaises(Exception):
            return self.assertEqual(counter(float), 4)

    def test_hard_input_three(self):
        with self.assertRaises(Exception):
            return self.assertEqual(counter(frozenset), 4)

    def test_hard_input_four(self):
        with self.assertRaises(Exception):
            return self.assertEqual(counter(list), 4)


if __name__ == "__main__":
    unittest.TestCase()
