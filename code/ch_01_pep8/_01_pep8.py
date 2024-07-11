# region import statements: os, some_module, etc...

# 1. Standard library imports first
# import itertools, subprocess, multiprocessing # Bad
import itertools
import multiprocessing  # Good
import os
import subprocess
import typing
# from os import path
from os import chdir, chmod, chown  # Good

# 2. PyPI Package imports
import requests

# 3. Our modules and submodule imports
from some_module import abort


# import requests
# import requests


# from some_module import abort
# from some_module import abort

# from os import * # Bad

# endregion

# region ******** Part 1 - imports **************************
# What does PEP 8 say about imports?
#
# One per line
# But multiple symbols are OK
#
#  Imports should be grouped in the following order:
#
#     standard library imports
#     related third party imports
#     local application/library specific imports
#
# You should put a blank line between each group of imports.
#

def some_func(): ...


# Prefer namespaces (i.e. os.path) over raw imports (i.e. path).
print(os.path.abspath(os.path.curdir))


# print(path.abspath(path.curdir))

# endregion

# region ******** Part 2 - code layout **************************
#
# Arranging classes, methods, and variables (lines between)
# Blank lines
# Surround top-level function and class definitions with two blank lines.
# Method definitions inside a class are surrounded by a single blank line.
# Use blank lines in functions, sparingly, to indicate logical sections.
#
# spaces, never tabs

def another_method(y):
    """
    Some details here...
    Args:
        y: The value of y

    Returns: No return value
    """
    x = 7
    if x == y:
        ...


another_method(7)
print(help(another_method))


def some_method_here():
    x = 1
    y = 1

    if x == y:
        print("They are the same")
    else:
        print("They are different")


def other_method():
    pass


def other_method2():
    pass


def other_method3():
    pass


class SomeClass:
    def m1(self):
        pass

    def m2(self):
        pass

    def m3(self):
        pass

    @classmethod
    def m4(cls):
        ...


# Line length <= 79? Probably more like 100
xd = ('ksdfj klsdjf lksjdflk sjdlkfj sdklfj sdkljf lksdjf  '
      'sldkjf sdkjf lskdj fjlks jdflkjs lkj lksjdf jkljsdklfj '
      ';klsdj fkl jsdfkljs dklfj sdklfj slkdklfj l')


# endregion

# region ******** Part 3 - Naming conventions ********************
#
# Modules should have short, all-lowercase names. Underscores can be used
# in the module name if it improves readability.
# import some_module
# print(some_module.abort)
# dice_role = 7

#
# Class names should normally use the CapWords convention.
#
# class SuperHero(Person):
#     ...

# Because exceptions should be classes, the class naming convention
# applies here. However, you should use the suffix "Error"
#
# class NoneError(Exception):
#     ...
#
# raise NoneError("Never do this ;)")

# Function names should be lowercase, with words separated by
# underscores as necessary to improve readability.
#
# Arguments
# Always use self for the first argument to instance methods.
# Always use cls for the first argument to class methods.

def yet_another_method(param1, person, other_person):
    ...


#
# If a function argument's name clashes with a reserved keyword,
# it is generally better to append a single trailing underscore rather
# than use an abbreviation or spelling corruption. Thus class_ is better than clss


def yet_another_method2(list_, name):
    ...


#
# Constants are usually defined on a module level and written in all capital
# letters with underscores separating words. Examples include MAX_OVERFLOW and
# TOTAL.
#
#

MAX_HOURLY_RATE = 25

MIN_HOURLY_RATE: typing.Final = 15
print(MIN_HOURLY_RATE)
MIN_HOURLY_RATE = 16  # Warning/error, don't change this value.


class BaseThing:
    def do_it(self, event_arg1):
        ...


class SpecializeThing(BaseThing):
    def do_it(self, _):  # Sometimes _ is the name for things we don't want to use.
        print("Specialized!")


#
#
#
#
#
# endregion
#
#
#
#
#
#
#
#

# region hide_errors [...]
hide_errors = [
    chdir,
    chmod,
    chown,
    abort,
    itertools,
    subprocess,
    multiprocessing,
    requests,
]
# endregion
