import unittest

import isbn_verifier


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

class IsbnVerifierTests(unittest.TestCase):
    def test_verify_isbn_example1(self):
        self.assertTrue(isbn_verifier.verify_isbn('3-598-21508-8'))

    def test_verify_isbn_example2(self):
        self.assertTrue(isbn_verifier.verify_isbn('0-19-852663-6'))

    def test_verify_isbn_example3(self):
        self.assertTrue(isbn_verifier.verify_isbn('1-86197-271-7'))

    def test_verify_isbn_example_with_X(self):
        self.assertTrue(isbn_verifier.verify_isbn('955-20-3051-X'))

    def test_verify_isbn_example3_no_delimiter(self):
        self.assertTrue(isbn_verifier.verify_isbn('1861972717'))

    def test_verify_isbn_example_with_X_spaces(self):
        self.assertTrue(isbn_verifier.verify_isbn('955 20 3051 X'))

    def test_verify_isbn_example4(self):
        self.assertTrue(isbn_verifier.verify_isbn('1-80097-271-7'))

    def test_verify_isbn_bad_example1(self):
        self.assertFalse(isbn_verifier.verify_isbn('1-80097-241-X'))

    def test_verify_isbn_bad_example2(self):
        self.assertFalse(isbn_verifier.verify_isbn('0-19-866663-6'))

    def test_verify_isbn_bad_example3(self):
        self.assertFalse(isbn_verifier.verify_isbn('0-19-852663-Z'))

    def test_verify_isbn_bad_example4(self):
        self.assertFalse(isbn_verifier.verify_isbn('019852663Z'))

if __name__ == '__main__':
    unittest.main()
