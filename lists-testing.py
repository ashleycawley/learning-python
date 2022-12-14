
my_list = [1,2,3,4,5,6,7,8,9,10]

print(type(my_list))

print(my_list)

# A Dictionary or 'dict' has to be declare and created with:
ash = dict() # Creates a new empty dictionary.

# Items in a dict are stored as:
# [ key ] = [ value ]

# Items can be added to a dict like this:
ash['name'] = 'Ashley'
ash['age'] = 34
ash['email'] = 'ash@ashleycawley.co.uk'
ash['score'] = 6.0

# Items can be retrieved with:
print("His name is:", ash['name'])

# However if you try to retrieve a item (key) that isn't in the dict it will
# result in a nasty error and python stopping execution, so there is a safer
# way to retrieve items using the var.get() function like this:
print(ash.get('county'))
# Even though there is no 'county' key it will just return "None" instead of stopping execution
print(ash.get('name'), '-', ash['email'])

