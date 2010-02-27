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
   its tests, if any.

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

---

Results of testing-in-python discussion, 2/27:

 - Matt Harrison: explicitly suggest placing test data (data used ONLY
   for tests) under the tests package directory.

 - Michael Foord: tests/ should be a package (contain an __init__.py),
   so that it is discoverable and Python can handle it.

 - Michal Kwiatkowski: explicitly suggest putting other tests in
   tests/ top-level directory.

 - Michal Kwiatkowski: also look at

      http://time-loop.tumblr.com/post/49578950/where-python-developers-keep-their-test-directories

   to see where people put their test directories.

 - Michael Foord: make the mechanism framework agnostic.

 - Titus Brown: rely on something other than specific module
   runtime semantics; so

     python setup.py test

   or something in the style of

     python -m somepackage.tests

   is better than 'python -m unittest somepackage' or whatnot.

 - All right thinking people agree that supporting suites from test
   tools other than unittest in setup.py would be nice.

 - Michael Foord: the 'suite' callable mentioned in unittest
   documentation isn't actually used or enforced, so it does not
   clash, collide, or make redundant the 'test_suite' collable
   convention defined in setuptools.

 - Michael Foord: for modules loaded with a TestLoader the load_tests
   function is better. For executing suites directly you can *now* do:
   python -m unittest package.module.suitename.

 - Michael Ford in response to Robert Collins: "So the real
   requirement is that the package / module specified should either be
   a standard unittest package - or provide a load_tests function that
   returns a unittest compatible TestSuite-like object, capable of
   being run with a TextTestRunner.

   If all test frameworks can adhere to this then I'm fine with dropping the
   'run' module requirement."

 - Michael Foord in response to Titus Brown: "load_tests is already a
   convention. This particular hook allows you to interoperate with
   unittest whilst avoiding most of the snakes. If you have *specific*
   problems with this approach then I'd like to hear about them. :-)"

 - Titus Brown: I should write up examples of using load_tests,
   test_suite (in setuptools), test_runner (in setuptools), discover
   (in unittest2/3rd-party package), and '-m unittest' (which may be
   redundant with one of the above?)

 - Titus Brown: I also don't really understand what the arguments to
   'setup.py test' are.

Longer e-mail from Michael:

> Perhaps the convention could be that you provide an executable run module
> only if the distutils2 defaults aren't adequate. In this case the
> arguments you supply in setup.py tests/testrunner arguments will have to
> do the same job as your run module (duplication).
>
> We could come up with a more complex scheme for distutils2 that meets all
> these usecases:
>
> If no arguments are specified in setup.py then "setup.py test" does the
> following:
> 
> For each package in the distribution that supplies a test sub-package
> including a run module, execute the equivalent of:
> 
> python -m package.test.run
> 
> For all packages that don't provide a test.run sub-package and module
> attempt test discovery.       
> 
> If tests/testrunner arguments are supplied to setup.py then those will be
> used and the programmer should also provide a test.run if he wants tests to
> be able to be run without setup.py being used.
> This kind of makes the setup.py arguments redundant, or at least slightly
> harmful to use them without providing test.run as well.

---

Concerns: how flexible is 'python setup.py test'?  Can it be framework
agnostic, or do frameworks have to expose a unittest-like framework
(e.g. what nose has done)?
