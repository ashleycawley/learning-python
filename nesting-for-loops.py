
## nesting for loops
numbers     = [1, 2, 3, 4]
letters     = 'abcd'

# pairs numbers and letters with one another using 'zip'
for number, letter in zip(numbers, letters):
    print(number, letter)
# Output would look like:
# 1 a
# 2 b
# 3 c
# 4 d

print()

for number in numbers:
    for letter in letters:
        print(number, letter)

for number in numbers:
    for letter in letters:
        for i in range(5):
            print(number, letter, i)

print(range(5))
print(list(range(5)))

sales = [
    list(range(3)),
    list(range(4)),
    list(range(5))
]
total = 0
print(sales)
print()
print(sales[1][2])
