import unittest

tests_are_in = 'a_package.some_tests'

class CustomTestLoader(object):
    def loadTestsFromNames(self, names, module=None):
        assert 'FOO' in names
        # ignore passed in 'names' for demo purposes.
        x = unittest.TestLoader().loadTestsFromNames([tests_are_in])
        return x
