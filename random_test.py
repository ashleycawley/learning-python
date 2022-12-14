# This script was just an experiment, it compares two randomly generated numbers picked between
# 1 - 1,000,000 to see how many combinations are tried before the two numbers collide and are
# the same. It increments a counter to tell you how many times it tried.

import random
import time
start_timer = time.process_time()
counter = 0
starting_random_number = random.randrange(1000001) # Picks a random number within 1,000,000

while not (starting_random_number == random.randrange(1000001)):
    counter = counter + 1
    print(counter)
    # time.sleep(0.001)

stop_timer = time.process_time()

print('It took', stop_timer-start_timer, 'seconds before the two random numbers between 1,000,000 colided.')