
## while loops

phrase = 'I love Phoebe'

index = 0
while index < len(phrase):
    letter = phrase[index]
    print(letter)
    index = index + 1

counter = 0

while counter < 5:
    print(counter)
    counter = counter + 1 # Increments the counter by 1 each time

## WHILE Loop continiously until a condition is met
while True:
    your_name = input('What is your name? ')
    if your_name == 'Ash' or 'Ashley':
        print('Access Granted - Welcome Ashley.')
        break
    else:
        print('Access Denied - Try Again...')

# An alternative method to the above is to:
running = True
while running: # NOTE: True is replaced with a variable.
    your_name2 = input('What is your name? ')
    if your_name2 == 'Ash':
        print('Access Granted - Welcome Ashley.')
        running = False # Condition was met so changing the var and thereby stopping the while loop
    else:
        print('Access Denied - Try Again...')
