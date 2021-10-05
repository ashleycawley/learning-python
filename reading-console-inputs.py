
## Reading Console Inputs

foods_prompt = """
Which food are you purchasing? (Choose a letter)
A) Banana
B) Apple
C) Cheese
D) Pickles
Q) Type Q to Quit.
Your Choice: """

while True:
    qty_prompt = """
How many do you need? (Enter a number)
Quantity: """

    food = input(foods_prompt)


    if food == 'Q':
        print('Goodbye!')
        break

    print(food)

    if food not in ['A','B','C','D']:
        print('Invalid Option. Try again.')
        continue
    else:
        quantity = int(input(qty_prompt))
        if quantity < 0:
            print('Quantity wrong')
            continue

        if food == 'A':
            cost = 0.30
            food_label = "Banana"
        elif food == 'B':
            cost = 1.00
            food_label = "Apple"
        elif food == 'C':
            cost = 3.00
            food_label = "Cheese"
        else:
            cost = 2.99
            food_label = "Pickles"

        total = cost * quantity
        result = "You are buying {} {} for £{}".format(quantity, food_label, total)
        print(result)