def recursive_loop(x):
    #base case , condition that terminates function execution 
    if x > 10:
        return
    print(x)
    x += 1
    #tail recursion : function acll is the alst statement 
    recursive_loop(x)


def is_palandrome(x, pos_index, neg_index):
    if x[pos_index] == x[neg_index]:
        print("")

    else:
        return False
    
    pos_index += 1  
    neg_index -= 1

    is_palandrome(x, pos_index, neg_index)

    print(is_palandrome('racecar', 0, -1))

is_palandrome('racecar', 0, -1)