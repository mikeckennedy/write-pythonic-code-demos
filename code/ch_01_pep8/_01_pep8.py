# ******** Part 2 - code layout **************************

# TODO: Arranging classes, methods, and variables (lines between)
# Blank lines
# Surround top-level function and class definitions with two blank lines.
# Method definitions inside a class are surrounded by a single blank line.
# Use blank lines in functions, sparingly, to indicate logical sections.











# TODO: Use 4 spaces per indentation level.
# spaces, never tabs



# TODO: 
# Limit all lines to a maximum of 79 characters. (still?)


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
# TODO: What does PEP 8 say about imports?

# One per line
# But multiple symbols are OK

#  Imports should be grouped in the following order:
#
#     standard library imports
#     related third party imports
#     local application/library specific imports
#
# You should put a blank line between each group of imports.











# There meaningless lines are here to prevent PyCharm from warning about
# unused imports and such. We want to see real warnings only. In a
# legitimate app, those other warnings would be useful but not here.

