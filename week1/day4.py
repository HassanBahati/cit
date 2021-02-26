#python Format with short of f

b1 = 'bread'
b2 = 'ham'
b3 = 'eggs'

#format method 1
print(f'For breakfast i had {b1}')
print(f'for breakfast i had {b2}')
print(f'for breakfast i had {b3}')

import time #time is inbuilt in python
def clock_time():
    count = 0
    start_time = time.time() #references the time function
        #count and stop after 1000 counts
    while count < 1000:
        now = time.time()#references the time function
        print(f'it has been {now - start_time} seconds since the loop started\n')
        count += 1
clock_time()
    
'''
the f in the print statement is a short form for format to enable us put functions

'''
