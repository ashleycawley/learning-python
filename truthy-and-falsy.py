#!/usr/bin/env python3

# Proper Boolean True/False
true_value = True
false_value = False

if true_value == True:      # NOTE: == Tests explicitly if it is the boolean True or False
    print('Its true')

if false_value == False:    # NOTE: == Tests explicitly if it is the boolean True or False
    print('Its False')

# Strings with contents can be consider True or Truthy, empty lists can be considered False or Falsey:
# Improper truethy variables:
true_value = "abc"          # NOTE: Truthy
false_value = []            # NOTE: Falsey

if true_value:              # NOTE: By missing off the == True part now we're just testing if it is Truthy
    print('Its truthy')

if not false_value:         # NOTE: Reverse the logic: "if not" to test for Falsey.
    print('Its Falsey')