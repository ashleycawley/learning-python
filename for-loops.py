
## for loops

names = ['Phil', 'Ash', 'Tim', 'Joe']

for person in names:
    print('Person:', person)

# Enumerate a list, outputting an index:
for index, person in enumerate(names):
    print(index, ':', names)

## loops can be shortened by using a underscore _ as the loop var placeholder, so the above could be:
for _ in names:
    print('Person:', _)

attempts = range(3)
fav_num = 7

for attempt in attempts:
    guess = int(input("What is your fav number? \n"))
    print(guess)
    ## This loop exits when the number of attempts matches the value (3) in the 'attempts' var

print('## Loop #1 Exited.')

for attempt in attempts:
    guess = int(input("What is your fav number? \n"))
    if guess == fav_num:
        print('Yay! You Win :-)')
        break
    else:
        print('Try Again! ...')
