### Operators ###

## Mathmatical Operators ##
# + and -
# / - Devide
# * - Multiply
# % - Modulas
# ** - Power operator
# // - Different type of devision

# +
print('3 + 1 is:', 3 + 1)

# -
print('3 - 1 is:', 3 - 1)

# /
print('6 / 2 is:', 6 / 2) # This sum gives a type conversion, we supply it
# integers but it actually outputs back 3.0 which is a floating point.

print('7 / 2 is:', 7 / 2) # Gives correct result (3.5) as floating point

# //
print('7 // 2 is:', 7 // 2) # Gives a truncated/dodgy result as a whole integer, NOT a floating point:
# // is an operator in Python3+ which mimicks the behavior of the / in older versions prior to Python3.
# In older versions of Python / used to just give you a integer back, it would cut-off the last bit after
# the decimal point, so instead of returning a floating-point to you it would return a whole integer.
# This means 7 / 2 in older versions would actually return to you just: 3 instead of the correct 3.5 answer.
# To mimick that same behavior today in modern day Python3+ then you can use // if you want to.

# % - Gives you the remainder when doing devision, for example: 2 goes into 7 three times whole but you're
# left with one remainder, so the following below would output one:
print('7 % 2 is:', 7 % 2)

# Where as 2 goes into 6 three times perfectly and there is no remainder so the following would output 0:
print('6 % 2 is:', 6 % 2)

# *
print('7 * 2 is:', 7 * 2)

# **
print('7 ** 2 is:', 7 ** 2)

print(2 ** 10) # Outputs: 1024
print(4 ** 5) # Outputs: 1024 | is the same at 4*4*4*4*4 (5 times)
print(4*4*4*4*4) # Outputs: 1024

## Comparison Operators ##

# Concatination Operator
print('hello'+'world') # Joins strings together without a space
print('a'+'b'+'c') # Joins strings together without a space
print('Ash ' * 6) # Repeats the string 6 times.

# Comparison
# <, <=, >, >=
# < - Less than
# <= - Less than or equal to
# > - Greater than
# > - Greater than or equal to
# == - exactly the same / matches
print(3 < 4)    # Asking a question: is 3 less than 4? Output will be a boolean: True
print(10 > 15)  # Output: False
print(4 == 4)   # Output: True

# Even words can be compared against one another and it will give True or False based on their alphabetical
# placement, for example:
print('Which comes first in the dictionary "Ash" or "Birch"? Does Ash come first? :', 'Ash' < 'Birch')
