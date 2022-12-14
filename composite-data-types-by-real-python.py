# NOTE: for standard data types (integer, boolean etc.) see file: data-types.py

### Composite Data Types - There are four composite data types in Python:
# 1. Lists
# 2. Dictionaries
# 3. Sets
# 4. Tuples

### List # NOTE: [ ]
numbers = [1, 2, 3, 4, 5] # List of numbers
strings = ['abc', 'xyz', 'qty'] # List of strings

### Dictionary # NOTE: {'key':'value'} colons and commas.
person_info = {"name": "Ashley", "age": 34, "hair": "Black", "height": 5.10}

# The same dictionary information can be represented across multiple lines to make it more readable:
person_info2 = {
    "name": "Ashley",
    "age": 34,
    "hair": "Black",
    "height": 5.10
}

# The value can be recalled by its value name or labe like:
print(person_info['age'])

# Dictionaries can also be placed onto one line like below, its just easier to interpret them across multiple lines.
choices = {"fruit": "apple", "qty": 8, "date": "24/10/2021"}
print("Fruit Type:", choices['fruit'], "\n"+"Best Before:", choices['date'])


### Set # NOTE: { }
fruits = {"apple", "banana", "cherry"}
# Sets allow you to store multiple items in one variable or data "set".
# NOTE: Sets are un-indexed, un-changable (cannot alter values) and cannot
# contain duplicates, subsequent duplicates are ignored.
# Sets can contain multiple different data-types, like:
mix = {"string", 4, 6.0, True}


### Tuple # NOTE: ( )
# Tuples are like sets in that they contain multiple items and are un-changeable,
# However they are indexed and do allow duplicate values which sets do not.
# Like a set a tuple can contain different data types within it:

tuple1 = ("abc", 34, True, "abc", 4.2)
tuple2 = ("apple", "pear", "orange", "pear")

# Because tuples are indexed their values can be recalled via numbers:
print(tuple1[2])
print(tuple2[1], tuple2[3])