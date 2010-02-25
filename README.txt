A simple example of my proposed "how to package tests" standard.  What do
you think?  --titus

--

To run the tests, you can do:

  % python -m somepackage.tests.run

under Python 2.5 or above, and

  % python setup.py test

if you have setuptools or Distribute installed.  This mechanism will also
be supported under distutils2, or distutils under 3.3 and above.

You can also run

  % nosetests

with nose.

How about py.test?  Other test runners?

---

Rules, in brief:
----------------

 - for a given package, 'python -m somepackage.tests.run' should run
   its tests, regardless of whether or not the 'tests' subpackage is
   installed.

 - no code outside of 'somepackage.tests' should depend on
   'somepackage.tests'.  This is so that distrib packagers (debian,
   redhat) can omit the sub-package from the non-devel install.

Rules, with a bit more exposition:
----------------------------------

Tests should generally be run at build time, but may not be runnable
after installation.  Nonetheless we want to specify how to do it in
case people want to install them.

As long as distrib packagers can remove the <package>/tests directory
from their distributed version of your package, they will be happy.
Therefore the rest of the package should not depend on anything in
<package>/tests.
