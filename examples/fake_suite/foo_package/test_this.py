class FakeTest(object):
    def __str__(self):
        return "my very long fake test"
    def shortDescription(self):
        return "i am short"

class FakeTestSuite(object):
    def __call__(self, result):
        the_test = FakeTest()
        
        result.startTest(the_test)
        result.addSuccess(the_test)
        result.stopTest(the_test)
    run = __call__

    def countTestCases(self):
        return 1

def load_tests(loader, standard_tests, x):
    return FakeTestSuite()
