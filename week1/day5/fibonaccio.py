def fib(r):
    a = 0
    b = 1
    print(a)
    print(b)

    for i range(r):
        temp = a      #temp = 1
        a = b    #a = 2
        b = temp + a # 1
        print(b)

# 0 1 1 2 3