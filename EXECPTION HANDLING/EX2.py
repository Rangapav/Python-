#
# What is an Exception?
# An Exception is an error that occurred during the execution of a piece of code.
# A runtime error is called an Exception, the cause of the exception is improper input.
# ---------------------------------------------------------------------------------------------------------
# Types of error in Python
# AssertionError	It occurs when an assert statement fails
# AttributeError	It occurs when attribute assignment fails
# FloatingPointError	It occurs when the floating-point operation fails
# MemoryError	It occurs when the operation is out of memory
# IndexError	It occurs when the order is out of range
# NotImplementedError	It occurs because of abstract methods
# NameError	When the variable is not found in the local or global scope
# KeyError	It occurs when the key is found in the dictionary
# ImportError	It occurs when the imported module is not present
# ZeroDivisorError	It occurs when the second operand is 0
# GeneratorExit	It occurs when the generator’s close() is
# OverFlowError	It occurs when the result of an arithmetic operation is too large
# IndentationError	It occurs when the indentation is not correct
# EOFError	It occurs when the input() function end in the file condition
# SyntaxError	It occurs when a syntax error is raised
# TabError	It occurs when inconsistent space or tabs
# ValueError	It occurs when the function gets a correct argument and an incorrect value
# TypeError	It occurs when the function or operation is incorrect
# SystemError	It occurs when the interpreter detects an internal error
#
# When error occurs exception is called, python will stop it and generates error message.
# The exception is handled by try, except and finally.
# try – It checks the error in the block of code
# except – It handles the error
# finally – It executes the code.
# ------------------------------------------------------------------------------
# Python Syntax Error
# Now, we can see syntax error in Python.
#
# In this example, I have used try to check the error in the block as the error is present in the syntax of print(python).
# The except is used as except SyntaxError as e. The except is executed.
# try:
#   print(python)
# except SyntaxError as e:
#   print("Invalid syntax")
# except:
#     print("Invalid syntax")