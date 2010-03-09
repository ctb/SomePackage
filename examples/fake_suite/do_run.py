import foo_package.test_this
suite = foo_package.test_this.load_tests(None, None, None)

import unittest, sys
result = unittest._TextTestResult(sys.stdout, 1, 1)
suite(result)
