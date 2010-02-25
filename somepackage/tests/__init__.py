# implement a basic test under somepackage.tests
import unittest

class TestSomething(unittest.TestCase):
    def test_something_else(self):
        self.assertEqual(True, True)
        
def get_suite():
    "Return a unittest.TestSuite."
    import somepackage.tests
    
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(somepackage.tests)
    return suite

