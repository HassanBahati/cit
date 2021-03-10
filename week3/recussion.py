#function simulates a loop by calling itself 

def recursive_loop(x):
    #base case , condition that terminates function execution 
    if x > 10:
        return
    print(x)
    x += 1
    #tail recursion : function acll is the alst statement 
    recursive_loop(x)

