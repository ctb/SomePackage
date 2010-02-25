try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup

setup(
    name='SomePackage',
    version='0.1.0',
    author='C. Titus Brown',
    author_email='titus@idyll.org',
    packages=['somepackage', 'somepackage.tests'],
    url='http://pypi.python.org/pypi/SomePackage/',
    license='LICENSE.txt',
    description='Useful package-test-related stuff.',
    test_suite='somepackage.tests.get_suite'
)
