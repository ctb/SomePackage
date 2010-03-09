from setuptools import setup

setup(
    name='A_Package',
    packages=['a_package'],
    # specifies a class that obeys the loadTestsFromNames(names, module)
    # convention of unittest.
    test_loader='a_package:CustomTestLoader',
    test_suite='FOO'                    # this will be passed in (and ignored)
    )
