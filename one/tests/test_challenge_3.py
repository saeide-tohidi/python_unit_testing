import sys
import unittest
from io import StringIO
from one.projects.challenge_3 import Printer


class TestPrintedOutPut(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        self.printer = Printer()

    def test_value_name(self):
        self.printer.set_value("Sara")
        self.printer.print_value()
        self.assertEqual(sys.stdout.getvalue().strip(), "Sara")
        pass

    def test_value_job(self):
        self.printer.set_value("Hello world")
        self.printer.print_value()
        self.assertEqual(sys.stdout.getvalue().strip(), "Hello world")
        pass

    def tearDown(self):
        self.printer = None
        pass


if __name__ == "__main__":
    unittest.main()
