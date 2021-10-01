# Sorting
numbers = [55, 34, 58, 220, 600, 456, 2, 1]

print(numbers)

# Sort contents of variable:
numbers.sort() # NOTE: It modifies the order of the original variable
print(numbers)

# Resetting the var back to be un-sorted just for demo purposes:
numbers = [55, 34, 58, 220, 600, 456, 2, 1]

# Setup new variable with sorted listed by using 'sorted()' function
# This allows you to have a new sorted list + keep the original 'numbers'
# variable intact so you have both to access if you need them.
sorted_numbers = sorted(numbers)

print(sorted_numbers)
print(numbers)

print()

# List of letters un-sorted
letters = ['c', 'e', 'f', 'b', 'g', 'a', 'd']
print(letters)

sorted_letters_asc = sorted(letters) # Sorted ascending: abcde...
sorted_letters_dsc = sorted(letters, reverse=True) # Sorted descending ..edcba
###### The "reverse=True" part above ^^^^^^^^^^^ is called a "Keyword Arguement"
print(sorted_letters_asc)
print(letters)
print()

# Reversing a list
names = ['Zak', 'Ash', 'Joe', 'Phil']
print('Normal order, not yet reversed:')
print(names, '\n')

reversed_names = list(reversed(names))
print(reversed_names)

names.reverse() # Reverse method - changes the order of the original var
print(names)

truth = [False, True, False, True, True, True, False]
print(truth)
sorted_truth = list(reversed(truth))
print(sorted_truth)
