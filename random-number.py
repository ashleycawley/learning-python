## Random Number
import random

print(random.randrange(100)) # Creates a random number up to 99

print(random.randrange(1000001)) # Picks a random number within 1,000,000

print(random.random()) # Gives you a random floating point number

# Random choice from a given list
names = ["Ash", "Claire", "Phoebe", "Phil", "Frankie"]
random_name = random.choice(names) # <-----
print(random_name)

secret_number = random.randint(1,100)

print(secret_number)