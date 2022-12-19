# PythonExponential
This is a simple code to evaluate the first n terms of the Maclaurin
Series of the exponential function. The idea of this repo is to
demonstrate the combination of unit testing and refactoring.

##exponential.py
Take a look at this code. It's the main code to evaluate the exponential function. You may
spot some ways to improve this function. Don't go ahead with these
changes yet - we're going to explore the unit tests first.

##Tests.py
This file contains the unit tests for the exponential function. The
idea is to evaluate the function at a few points and compare it to the
known values of e^x.

Running this file produces a failed test. The function doesn't give
the correct value of e^1 to enough decimal places. This is not a bug
in the code but a problem with the test. Correct the test so that it
uses more terms in the Maclaurin series and verify that it now passes
the test.

###Add some further tests.
Copy and paste the test function and create a new test to check the
value at x=0. Repeat this to create a 3rd test at x=2. Now run the
tests and check that all 3 tests pass.

###Commit these changes.
It would now make sense to commit your changes.

##Test coverage
The script coverageTest.sh runs the test a reports on which lines have
been run. The idea is to be sure that every line run during the
tests. Run the script (you may need to run pip install coverage before
this will work). If you can't get coverage to install you can still
move to the next stage. If the tests don't run every line can you
understand why this is ok for this code?

##Refactoring
We're now going to try to improve the function eval_exp. Take a look
at the code for this function - can you see any possible
improvements. Possibility are using the 'sum' function to avoid one of
the loops, using a list comprehension to fill the 'terms' list, or
removing entirely the need for the 'terms' list. Make the changes that
make the most sense to you, checking that the test pass after each
change to make.
