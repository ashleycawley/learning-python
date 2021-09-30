
## Our First List
names = ['Ash', 'Claire', 'Ryan']

print('People: ', names[1])


# Number of items (length) of things in the 'names' list
print('Number of items: ', len(names))

# The len function (for length) can be used on strings too:
print('Ashley has: ', len('Ashley'), 'number of characters in his name.')

dog_names = 'Phoebe Bosun Denzil Barney'
dog_names_list = list(dog_names) # Breaks each character ^ in a list
print(dog_names_list[2]) 
