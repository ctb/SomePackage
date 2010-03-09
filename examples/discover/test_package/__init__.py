import unittest

class YetAnotherTestCase(unittest.TestCase):
    def test_foo(self):
        pass

def load_tests(loader, standard_tests, x):
    # just return standard_tests, which is the set of tests that would
    # ordinarily be loaded in the absence of load_tests; no other tests
    # will be loaded from within this package (i.e. recursively) unless
    # you explicitly load them.
    
    return standard_tests
