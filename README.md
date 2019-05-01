# JVPM
To run a class file input the following command:

$ python jvpm/main.py {filename}

where filename.class is the class file you want to run.


This repo has a simple 'Hello World' program in Python 3. To run the
program, do
```
$ python3 jvpm/HelloWorld.py
Hello world
```

As with all good programs, there are unit tests for Test-Driven Development
included. To run the tests, do
```
$ python3 -m unittest
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```

We use test code coverage tools to make sure we are covering as much of the
program as possible with the tests. To generate the test code coverage, do
```
$ coverage run -m unittest
```

To view the results, do
```
$ coverage report
Name                           Stmts   Miss  Cover
--------------------------------------------------
jvpm/HelloWorld.py                 4      1    75%
jvpm/__init__.py                   0      0   100%
jvpm/test/__init__.py              0      0   100%
jvpm/test/test_HelloWorld.py       9      0   100%
--------------------------------------------------
TOTAL                             13      1    92%
```
Also, within this program we are in the beginnings of building a JVM with python. Sprint 2 includes reading header information and opcodes to the methods.

So far have a python program JVPM.py that can extract to the Constant count. Also, included are some tests to verify programs validity. Will be adding more to the Readme as time goes on.
