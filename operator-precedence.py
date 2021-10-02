
## Operator Precedence

names = ['Ash', 'Joe', 'Phil', 'Nathan']

# in - test if a name is 'in' a list. Answer is boolean (True/False)
print('Is Phil in the club?', 'Phil' in names)
print('Is Tim in the club?', 'Tim' in names)
print('Tim is not in the club:', 'Tim' is not names)

# is
print('phil' is 'phil')

fav_food =      'cheese'
lunch_today =   'cheese'

print(fav_food is lunch_today) # This is kind of like a question: Is fav_food lunch_today?

# NOTE: When comparing a string like above it checks they're the same, but the same 'is'
# technique cannot be used when comparing lists against each other, for that you should
# use something else, see below:

## Compairing exact values should be done with ==

fav_food =      ['cheese', 'crackers', 'jam']
lunch_today =   ['cheese', 'crackers', 'jam']

# To illustrate the issue discussed above, these will give different results:
print(fav_food is lunch_today) # False
print(fav_food == lunch_today) # True

# Summary: == is the best for comparing lists against one another.

# not operator
print(not 1 == 1) # False | The not at the front flips the logic
print(1 != 1) # False |

# Summary: Avoid 'not' where possible and stick to != instead.
