# Tripple Quoted Strings
# Using: """ text""" or '''text'''
# Is used for multi-line text but has the added benfit of ignoring internal quotes without escaping:
print("""this will "work" fine""")
print('''so will "this" and that's great''')
print("""This is a example
of a multi-line string
It is cool""")

# the "r" signifies a raw string and stops slashes from being interpreted
print(r"example of raw \n string")