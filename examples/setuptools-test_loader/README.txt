An example of using setuptools' test_loader attribute; see 'setup.py'
where 'test_loader' is set to 'a_package:CustomTestLoader', and
'test_suite' is set to 'FOO' (and ignored, in this case).

See

http://peak.telecommunity.com/DevCenter/setuptools#test-loader

for more details.

Run the tests like so::

  % python setup.py test

You'll need to have setuptools or distribute installed.
