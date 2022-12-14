#!/usr/bin/env python3




list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5,6,7,8,9,10]
tuple1 = ('apple', 'pear', 5, 8)
string1 = "one two three four five"
dictionary1 = {'key': 'value', 'fruit': 'pear'}

print(len(list1))
print(len(tuple1))
print(len(string1))
print(len(dictionary1))

# An example of using len() to check for boundary condition, the function below
# Checks the username is between 4 and 10 characters long:
def check_username(username):
    return 4 <= len(username) <=10

print(check_username("ash"))

# A function which continues to request names from the user until it has three
# A while loop which checks the length of a list.
def get_names():
    names = []
    while len(names) < 3:
        name = input("Enter a name: ")
        names.append(name)
    return names

print(get_names())

# Retrieving the last item from a tuple, using the tuple1 length -1 because of zero-indexing
print(tuple1[len(tuple1)-1])

print(tuple1[-1]) # This is another trick to do the same thing but without len()

# Finding the mid-point
print(list2[len(list2) // 2]) # One / would give a float and wouldn't work // gives a int