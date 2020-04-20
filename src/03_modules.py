"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import platform
import os
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE


for arg in sys.argv:
    print(arg)


# Print out the OS platform you're using:
# YOUR CODE HERE


op_system = platform.system()
print(f"Operating System: {op_system}")


# Print out the version of Python you're using:
# YOUR CODE HERE
py_version = sys.version
print(f"Python Version: {py_version}")


# See the docs for the OS module: https://docs.python.org/3.7/library/os.html


# Print the current process ID
# YOUR CODE HERE


process_id = os.getpid()
print(f"Process ID: {process_id}")


# Print the current working directory (cwd):
# YOUR CODE HERE


cwd = os.getcwd()
print(f"Current Directory: {cwd}")


# Print out your machine's login name
# YOUR CODE HERE
login = os.getlogin()
print(f"User: {login}")