# Scope
a = 'one'
b = 'two'
c = 'three'

print(globals())

def myfunction():
    print('function running...')
    print(globals())

myfunction()

print(globals())
print(globals())
print(globals())