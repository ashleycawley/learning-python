### My very basic Python examples ###

## Variables
number  = 8         # Integer
name    = 'Julie'   # String
sunny   = True      # Boolean
result  = 20.85     # Floating point


# Testing the type of value in a variable:
print(type(result)) # Would output: <class 'float'>


## Lists
number_list     =   [ 1, 2, 3, 4, 5 ] # List of integers
letter_list     =   [ 'a', 'b', 'c' ] # List of strings
dog_names = [
    'Phoebe',
    'Bosun',
    'Denzil'
] # A list can also be written across multiple lines like this ^
# Items need the comma after them apart from the last item in the list.


## Increment a integer variable
num = 1
num = num + 1 # Adds 1 onto num


## FOR Loop
names = ['Phil', 'Ash', 'Tim', 'Joe']
for person in names:
    print('Person:', person)
    

## Do something for X number of times, 5 in this example:
for times in range(5):
    print('Go!')


## Stop a Loop - BREAK
letters = [ 'a', 'b', 'c' ]
for something in letters:
    print(something)
    if something == 'b': # Stops it from reaching 'c'
        break


## WHILE Loop
counter = 0
while counter < 5:
    print(counter)
    counter = counter + 1 # Increments the counter by 1 each time
# This while loop would run 5 times, outputting: 0, 1, 2, 3, 4


## WHILE Loop continiously until a condition is met
while True:
    your_name = input('What is your name? ')
    if your_name == 'Ash' or 'Ashley':
        print('Access Granted - Welcome Ashley.')
        break
    else:
        print('Access Denied - Try Again...')


## Reading Files - Four Methods:

# This one is for older python and is a bit more cumbersome:
file = open('/home/acawley/Documents/python/learning-python/file.txt', 'r')
for line in file:
    print(line)
file.close()


# This one puts each line into a list, even blank lines will be stored as items in the list like '\n'
file = open('/home/acawley/Documents/python/learning-python/file.txt', 'r')
lines =file.readlines()
print(lines)
file.close()


# This prints the text as just a block of text
file = open('/home/acawley/Documents/python/learning-python/file.txt', 'r')
text = file.read()
print(text)
file.close()

# With this method you do not have to close the file with file.close() because this method
# has in-built clean-up. This is called a "Context Manager"
with open('/home/acawley/Documents/python/learning-python/file.txt', 'r') as file:
    for line in file:
        print(line)

## Writing and Copying Files
with open('my-file.txt', 'w') as file:
    file.write('hello world')
# NOTE: 'w' stands for write and it blanks the file when starting

# Append to the end of the file:
with open('my-file.txt', 'a') as file:
    file.write('hello world')
# NOTE: 'a' - is what makes it append to the end of the file


## Copying a File
with open('source-data.txt', 'r') as input_file:
    with open('destination-data.txt', 'w') as output:
        for line in input_file:
            output.write(line)
            
# The same statement can be written in a different layout:
with open('source-data.txt', 'r') as input_file, open('destination-data.txt', 'w') as output:
        for line in input_file:
            output.write(line)
