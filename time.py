from time import process_time

num = 50000
start_timer = process_time()

for i in range(num):
    print(' ')
    # time.sleep(0.01)

stop_timer = process_time()

print('Script took:', stop_timer-start_timer)
