# Writing to a file

# NOTE: You have to be careful when opening files for writing in Python, even if you do
# nothing with the file like this example below it will effectively ERASE the contents:

with open('file2.txt', 'w') as file:
    print('not doing anything')