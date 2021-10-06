# Keywords and Positional Arguements

def game(starting_score=15, player_name='Player 1'):
    print('Starting Score: ', starting_score)
    print('Player Name: ', player_name)

game(starting_score=200)

def example(*args, **kwargs):
    #print(*args)
    #print(**kwargs)
    first_name = kwargs['first_name']
    last_name = kwargs['last_name']
    age = kwargs['age']
    print('Hello', first_name, last_name, 'you are', age, 'years old.')


#example(1,2,3,4,5)
example(first_name='ashley', last_name='cawley', age=34)