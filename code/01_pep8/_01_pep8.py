# ******** Part 2 - code layout **************************


class AClass:
    def m1(self):
        pass

    def m2(self):
        pass

    def m3(self):
        pass


def some_method(a1, a2, a3):
    """
    some_method returns the larger of 1 or 2

    :param a1: First item to compare
    :param a2: Second item to compare
    :param a3: Should reverse
    :return: 1 or 2
    """
    x = 1

    if x > 2:
        return 1
    else:
        return 2


some_method(1, 1, 2)


def other_method():
    pass


def other_method2():
    pass


def other_method3():
    pass


s = "Text"

















# Use 4 spaces per indentation level.
# spaces, never tabs
def method():
    four_spaces_indented = True
    more_vars = 1


# Limit all lines to a maximum of 79 characters.
text = "This is a string which is longer than 79 characters. This is not encouraged but will execute and run OK."

# blank lines
# Surround top-level function and class definitions with two blank lines.
# Method definitions inside a class are surrounded by a single blank line.
# Use blank lines in functions, sparingly, to indicate logical sections.

# ******** Part 3 - Naming conventions **************************

# Modules should have short, all-lowercase names. Underscores can be used
# in the module name if it improves readability.

# Class names should normally use the CapWords convention.

# Because exceptions should be classes, the class naming convention
# applies here. However, you should use the suffix "Error"

# Function names should be lowercase, with words separated by
# underscores as necessary to improve readability.

# Arguments
# Always use self for the first argument to instance methods.
# Always use cls for the first argument to class methods.

# If a function argument's name clashes with a reserved keyword,
# it is generally better to append a single trailing underscore rather
# than use an abbreviation or spelling corruption. Thus class_ is better than clss

# Constants are usually defined on a module level and written in all capital
# letters with underscores separating words. Examples include MAX_OVERFLOW and
# TOTAL.










# ******** Part 1 - Imports **************************
import collections

# no: import collections, os, multiprocessing
# import collections
# import os
# import multiprocessing


# from my_module import path
from os import chdir, chflags, chown

# from os import *

# ERROR:
# import sys, os, multiprocessing

# But multiple symbols are OK

#  Imports should be grouped in the following order:
#
#     standard library imports
#     related third party imports
#     local application/library specific imports
#
# You should put a blank line between each group of imports.


# Wildcards:
# no: import collections, os, multiprocessing










# There meaningless lines are here to prevent PyCharm from warning about
# unused imports and such. We want to see real warnings only. In a
# legitimate app, those other warnings would be useful but not here.
s = sys
o = os
m = multiprocessing
z = path
z = chmod
z = chown
m = mean
c = collections
