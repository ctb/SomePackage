import unittest

class AnotherTestCase(unittest.TestCase):
    def test_foo(self):
        pass

def load_tests(loader, standard_tests, x):
    # here, you can either use 'loader' to load tests however you want,
    # e.g.
    suite = loader.loadTestsFromTestCase(AnotherTestCase)

    # this suite can now be returned:
    return suite

    # or you can just return standard_tests, which is the set of tests
    # that would ordinarily be loaded in the absence of load_tests.
    
#    return standard_tests
