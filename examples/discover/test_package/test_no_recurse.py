import unittest

class FailingTestCase(unittest.TestCase):
    def test_fail(self):
        self.assertEquals(0, 1)
