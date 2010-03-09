import unittest

class TheTestCase(unittest.TestCase):
    def test_foo(self):
        pass

def load_suite():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TheTestCase)
    return suite
