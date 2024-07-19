# Markdown text used as conditional appends

OVERVIEW = """
## Overview
You are a code assistant that accepts a {language} test file, and a {language} included files.
Your goal is to generate one and only one additional unit test to complement the existing test suite, 
in order to increase the code coverage against the source file.
"""

TEST_FILE = """
## Test File
Here is the test file that you will be writing tests against, called `{test_file_name}`.
=========
{test_file}
=========
"""

INCLUDED_FILES_PROMT = """
## Included Files
Here are the included files that you will be writing tests against.
Note that we have manually added line numbers for each line of code, to help you understand increasing code coverage.
Those numbers are not a part of the original code.
"""

INCLUDED_FILE = """
FILE NAME : {included_file_name} =====
{included_file_with_line_numbers}
======================================
"""
