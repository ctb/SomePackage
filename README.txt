A simple example of my proposed "how to package tests" standard.  What do
you think?  --titus

--

To run the tests, you can do:

  % python -m somepackage.tests.run

under Python 2.5 or above, and

  % python setup.py test

if you have setuptools or Distribute installed.

You can also run

  % nosetests

with nose.

How about py.test?  Other test runners?

---

Rules:

 - for a given package, 'python -m somepackage.tests.run' should run its tests;

 - no code outside of 'somepackage.tests' should depend on 'somepackage.tests',
   so that distribution packagers can omit the sub-package.
