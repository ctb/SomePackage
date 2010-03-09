An example of using setuptools' basic test_suite callable; see
'setup.py' where 'test_suite' is set to 'a_package.load_suite', and
the function 'load_suite' in a_package/__init__.py.

Here, 'test_suite' is pretty flexible; see:

http://peak.telecommunity.com/DevCenter/setuptools#test-build-package-and-run-a-unittest-suite

for details.

Run the tests like so::

  % python setup.py test

You'll need to have setuptools or distribute installed.
