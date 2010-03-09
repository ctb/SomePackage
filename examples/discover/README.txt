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

Note, you can run all three tests properly with

  % python -m discover -p 'test*'

Even when 'test_package' is examined for tests, the file
'test_package/test_no_recurse.py' is not -- this is because the
function 'test_package.load_tests' exists.  If you rename 'load_tests'
to something else, than four tests are found (and the one in
test_no_recurse.py fails, as it is supposed to).
