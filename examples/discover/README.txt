Examples of using 'discover', the 2.7+ test discovery mechanism.  You'll
need to install the 'discover' package for 2.4-2.6.

For example, from this directory, running

  % python -m discover -v

shows ::

   test_me (the_package.test_something.MyTestCase) ... ok
   test_foo (the_package.test_with_loader.AnotherTestCase) ... ok

It doesn't find the test inside of 'test_package', however, because
it's trying to match 'test_package' to the pattern 'test*.py'.  See
discover.py, line 146.
