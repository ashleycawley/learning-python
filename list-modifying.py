## List of names
names = ['Ash', 'Claire', 'Ryan', 'Jon', 'Frankie', 'Joe']
print('Names: ', names)

## Appending something to the end of a list
names.append('Babs')
print('Names: ', names)

# Removing an item:
names.remove('Ryan') # Specific item by precise value
del names[2] # Removing a item based on its indexed number in the list
print('Names: ', names)

# Removes the last item from the list:
names.pop()
print('Names: ', names)

names.pop(0) # Removes item 0 (the first item) from list 
print('Names: ', names)

# Replace an item in the list with a different value
# In this example replace Frankie with Phil
names[1] = 'Phil'
print('Names: ', names)
