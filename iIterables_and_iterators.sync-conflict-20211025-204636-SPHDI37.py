
# Setting up a list of items
numbers = [1,2,3,4,5,6,7]

# Number of items in the list can be found with:
len(numbers)

# Outputting this:
print(len(numbers))

# 'any'

all_true = [True, True, True]
some_true = [True, False, True]
all_false = [False, False, False]

# any()
print(any(all_true)) # Outputs True
print(any(some_true)) # Outputs True - because it contains at least one True value
print(any(all_false)) # Outputs False

# all()
print(all(all_true)) # Outputs True
print(all(some_true)) # Outputs False - because not all items are True
print(all(all_false)) # Outputs False - because there are no Trues

# Reversing a list with: reversed()
numbers_reversed = reversed(numbers)

# If displaying the reversed list we need to use list()
print(list(numbers_reversed))