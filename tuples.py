#!/usr/bin/env python3

# A Tuple is a collection of Python objects separated by commas.
#
# Tuples can contain different data types and even have other objects
# (like other tuples) nested within them.
#
# Tuples are immutable, they cannot be changed once they are created.
#
# Tuples can be created, combined and deleted.
#
# In someways a tuple is similar to a list in terms of indexing,
# nested objects and repetition but a tuple is immutable unlike lists which are mutable.

# Comma separated:
my_tuple = ('apple', 'pear', 'orange')

# Tuples can contain mutiple different data types:
second_tuple = (5, 'fruit', 4.25)

print(my_tuple) # Showing all items in the tuple:

print(my_tuple[0]) # Showing the first item in the tuple

# Combining two tuples into one:
combined_tuple = my_tuple+second_tuple 

print(combined_tuple)

del my_tuple # Deleting a Tuple

# Repeating data within a Tuple can be done by multiplying it:
big_data = ('dog', 'cat', 'bear', 'fish')*50
print("There are:", len(big_data), "items within big_data, look:")
print(big_data)

list1 = [1,2,3,4,5] # A List
new_tuple = tuple(list1) # Converts a List into a Tuple
print(new_tuple)