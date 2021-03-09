def loop(x):
    print(x)
    x -= 1
    loop(x)

loop(100)

'''
without using , prrint out 0 - 99

-call the function without itself
-solve the overflow error
'''
