import unittest
import xl


class TestXl(unittest.TestCase):
    def test_header(self):
        self.assertEqual(
            xl.read_column_headers("fname.xls"), ["name", "address", "phone"]
        )

    def test_col(self):
        self.assertEqual(xl.read_column("fname.xls", "name"), ["Alice", "Bob"])
