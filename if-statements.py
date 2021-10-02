
## if statements

veg = False

if veg == True:
    print('Little Tim has eatten his Veg! Time for ice cream.')

if veg == False:
    print('Little Tim has not eaten his Veg, no afters for him :-(')

# As this is a boolean true/false answer the if statement can actually be truncated:
# You can drop the: == True or == False part, see below:
peas = True

if peas:
    print('Little Tim has eatten his peas! Time for ice cream.')

if not peas:    # NOTE: added 'not'
    print('Little Tim has not eaten his peas, no afters for him :-(')

## if else
plate = True

if plate:
    print('The plate is clean!')
else:
    print('The plate is still dirty and has food on it')
