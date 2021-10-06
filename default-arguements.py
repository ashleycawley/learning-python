## Default Arguements

def speak(food=None):
    if food is None:
        print('Nom nom nom!!')
    else:
        print('I had some {}'.format(food))

speak('cheese')

speak('bread')