import sys
from io import StringIO
import unittest
from one.projects.third_project import Profile


class TestPrintedInput(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        self.profile = Profile("Saede", 33, "developer")

    def test_name(self):
        self.profile.print_name()
        self.assertEqual(sys.stdout.getvalue().strip(), "Saede")

    def test_job(self):
        self.profile.print_job()
        self.assertEqual(sys.stdout.getvalue().strip(), "developer")

    def test_age(self):
        self.profile.print_age()
        self.assertEqual(sys.stdout.getvalue().strip(), "33")

    def TearDown(self):
        self.profile = None


if __name__ == "__main__":
    unittest.main()
