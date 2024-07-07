# Markdown text used as conditional appends
ADDITIONAL_INCLUDES_TEXT = """
## Additional Includes
The following is a set of included files used as context for the source code above.
This is usually included libraries needed as context to write better tests:
======
{included_files}
======
"""

ADDITIONAL_INSTRUCTIONS_TEXT = """
## Additional Instructions
======
{additional_instructions}
======
"""

FAILED_TESTS_TEXT = """
## Previous Iterations Failed Tests
Below is a list of failed tests that you generated in previous iterations.
Do not generate the same tests again, and take the failed tests into account
 when generating new tests.
======
{failed_test_runs}
======
"""

OVERVIEW = """
## Overview
You are a code assistant that accepts a {language} source file, and a {language} test file.
Your goal is to generate additional unit tests to complement the existing test suite, 
in order to increase the code coverage against the source file.
"""

SOURCE_FILES = """
## Source File
Here is the source file that you will be writing tests against, called `{source_file_name}`.
Note that we have manually added line numbers for each line of code, to help you understand the code coverage report.
Those numbers are not a part of the original code.
=========
{source_file_numbered}
=========
"""