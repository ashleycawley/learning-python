# Boleans are True or False, the first character being a capital IS important in Python
# In Python True/False can also be represented as a number:
# 0 - False
# 1 - True

state = True

# A boolean can be evaluated with the bool() function:
bool(state)

if state == True:
    print('Yes state is true')

# Shortened logic check:
if state:
    print('Yes state is still true and this was a shorter way of finding out.')

if state:
    print('state is True')
else:
    print('state is False')