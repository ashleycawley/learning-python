## Defining Functions

# Most Basic Function - Defining it:
def speak():
    print("Lets talk about food")

# Invoking and using the function:
speak()

# Defining a function to use supplied arguments:
def speak(food):
    print('Lets eat: ' + food )
    print('I enjoyed that {}'.format(food))

# Invoking the function and providing arguements:
speak('pizza')
speak('chocolate')
speak('cheese')