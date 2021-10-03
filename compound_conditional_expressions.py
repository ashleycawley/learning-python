
## Compound Conditional Expressions

eaten_peas = True
eaten_carrots = True
eaten_sprouts = True

# An example of a nested 'if' that not a compound expression
if eaten_peas:
    if eaten_carrots:
        print('You get ice cream')
    else:
        print('Nothing for you!')

print()

# and - compound conditional expression with a 'and'
if eaten_peas and eaten_carrots:
    print('You get ice cream')
else:
    print('Nothing for you!')

print()

# or - compound conditional expression with a 'or'
# Otherwise known as an "Inclusive or"
if eaten_peas or eaten_carrots:
    print('Well you ate one of them, so that is good enough.')
else:
    print('Nothing for you!')

# or - An Exclusive or :
give_me_money = True
fuel_my_car =   False

# Checks that one or the other is done BUT NOT both
if (give_me_money or fuel_my_car) and not (give_me_money and fuel_my_car):
    print('Thank you!')
else:
    print('You shouldn\'t cover both, thats too much!')

# Summary: There is three eventualities from the above: If netier is done (both False) then
# there is no thank you or output, if one is done it says Thank You! If both is done it says
# that was too much.

# The same as above can be achieved but the first line made simplier by breaking the 'or' and
# the 'and' apart, with one being a elif:
if give_me_money and fuel_my_car:
    print('You shouldn\'t cover both, thats too much!')
elif give_me_money or fuel_my_car:
    print('Thank you!')
else:
    print('I\m going to need a hand with fuel')
# Summary: the logic in this latter one is simplier to read and digest.
    
