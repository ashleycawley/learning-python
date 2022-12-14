# Setting up a list of items
numbers = [1,2,3,4,5,6,7]

# Number of items in the list can be found with:
len(numbers)

# Outputting this:
print(len(numbers))

# 'any'
all_true = [True, True, True]
some_true = [True, False, True]
all_false = [False, False, False]

# any()
print(any(all_true)) # Outputs True
print(any(some_true)) # Outputs True - because it contains at least one True value
print(any(all_false)) # Outputs False

# all()
print(all(all_true)) # Outputs True
print(all(some_true)) # Outputs False - because not all items are True
print(all(all_false)) # Outputs False - because there are no Trues

# Reversing a list with: reversed()
numbers_reversed = reversed(numbers)

# If displaying the reversed list we need to use list()
print(list(numbers_reversed))

# range(30) - for creating a range of numbers, encapsulated within a list() to
# put the numbers into a list. NOTE: It is exclusive, goes from 0-29 missing 30.
my_num_range_list = list(range(30))
print(my_num_range_list)

# Enumerate a list

# One was to enumerate and display a list of indexes against their values would be:
players = ['Ash', 'Phil', 'Joe', 'Frankie']
counter = 0
for player in players:
    print(counter, player)
    counter =+ 1
# However a better way using the enumerate() function would be:
for count, player in enumerate(players):
    print(count, player)

# ZIP - In this example we have two lists that need to be paired together
list1 = ["192.168.1.5", "192.168.1.6", "192.168.1.7", "192.168.1.8"]
list2 = ["Ashley-PC", "Ashley-Laptop", "Claires-PC", "Claires-Laptop"]

merged_list = zip(list1, list2)
print(list(merged_list))

# Iterator
a = iter([1,2,3,4,5])