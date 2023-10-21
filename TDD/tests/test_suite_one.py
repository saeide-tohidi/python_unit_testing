import unittest
from TDD.tests.test_wealth_manager import TestCalculate


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestCalculate('test_calculate_medium_first'))
    suite.addTest(TestCalculate('test_calculate_easy_first'))

    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())