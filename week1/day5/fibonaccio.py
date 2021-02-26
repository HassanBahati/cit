'''
fibonaccio sequence 
'''
#defining the finction fib with parameter r 
def fib(r):
    a = 0
    b = 1
    print(a)
    print(b)
#for loop
    for i in range(r):
        temp = a      #temp = 1
        a = b    #a = 2
        b = temp + a # 1
        print(b)

# 0 1 1 2 3 5
#invoking the function
#fib(4)


#declaring the function
def hassan(r):
#variables can assigned on same line 
    a, b = 0, 1
#for loop
    for i in range(r):
        print(a)
        a, b = b, a + b
#invoking the function
hassan(6)


'''
when solving algorithms , thinks of all the tests
think how to solve it automativcally

read the description 
what are the variables 
brute force solutions , have running code
'''