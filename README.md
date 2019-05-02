# Java Virtual Machine

This repo has a java virtual machine program, taking in a .class file and running
the program as a JVM would. This JVM is written in Python and can run java programs
that include basic arithmetic and printing of strings.  

## Installing

To get a development env running install: codecov, numpy, coverage, bitstring, unittest, and binascii.
```
$ pip install numpy
Collecting numpy
Downloading https://files.pythonhosted.org/packages/4e/9d/c129d78e6b942303b762ccfdf1f8339de80c5e6021b14ef0c99ec5bdc6aa/numpy-1.16.3-cp37-cp37m-win_amd64.whl (11.9MB)
100% |████████████████████████████████| 11.9MB 865kB/s
Installing collected packages: numpy
Successfully installed numpy-1.16.3
```
and repeat until finished.

To download (right click and save as) pip download get-pip.py file https://bootstrap.pypa.io
making sure to save as a .py file. Navigate to the folder containing the file
and run the command:
```
$ python get-pip.py
Collecting pip
Using cached https://files.pythonhosted.org/packages/f9/fb/863012b13912709c13cf5cfdbfb304fa6c727659d6290438e1a88df9d848/pip-19.1-py2.py3-none-any.whl
Collecting wheel
Downloading https://files.pythonhosted.org/packages/96/ba/a4702cbb6a3a485239fbe9525443446203f00771af9ac000fa3ef2788201/wheel-0.33.1-py2.py3-none-any.whl
Installing collected packages: pip, wheel
Successfully uninstalled pip-19.1
Successfully installed pip-19.1 wheel-0.33.1
```

## Getting Started

To run the JVPM use command below, HelloWorld can be replaced with any
class file name. The file must be in the javafiles folder in jvpm; ".class" post-fix
is added by the program.
```
$ python3 jvpm/main.py HelloWorld
HelloWorld!
```

To create a .class file from a .java file, navigate to the directory containing the java file.
Run the command below:
```
$ javac HelloWorld.java
```
In order to run the javac command you must add the jdk bin filder to PATH, read:
https://stackoverflow.com/questions/1678520/javac-not-working-in-windows-command-prompt

## Running unittests

To run unittest, use command below.
```
$ python3 -m unittest
......
----------------------------------------------------------------------
Ran 48 tests in 0.329s

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
Name                                                 Stmts   Miss  Cover
------------------------------------------------------------------------
jvpm\__init__.py                                         0      0   100%
jvpm\packages\CPInfo.py                                 82     16    80%
jvpm\packages\__init__.py                                1      0   100%
jvpm\packages\access_flag_translater_dictionary.py       4      0   100%
jvpm\packages\jvpm_dict.py                               7      0   100%
jvpm\packages\jvpm_methods.py                          144     18    88%
jvpm\packages\jvpm_opcodes.py                          147     15    90%
jvpm\packages\pool_methods.py                           40      0   100%
jvpm\packages\pool_translate.py                        167     12    93%
jvpm\packages\read_attribute.py                        125     13    90%
jvpm\packages\stack.py                                  13      0   100%
test\__init__.py                                         0      0   100%
test\test_jvpm.py                                      685      3    99%
------------------------------------------------------------------------
TOTAL                                                 1415     77    95%
```

### Contributors
* drsjb80
* LSmith-Zenoscave
* zkhalido
* Cjohnson187
* G-Leib
* DominickNola
* minouye2
* Azuesflip
* elopezh1

All contributors can be found on GitHub.  
