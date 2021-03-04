'''
define a function
wrtie a tuple 1,2,3,4,5,6,7,8,9,10,10,11,12
replace 5 with a
remove two 10s from the tuple 
return the modified tuple
note : tuples can also be created without parentheses
'''



def my_tuple():
    #defining the tuple
    my_tuple = (1,2,3,4,5,6,7,8,9,10,10,11,12)
    #converting the tuple to a list
    my_list = list(my_tuple)
    #replacing 5 with a 
    my_list[4] = 'a'
    #removing the 1st 10
    my_list.remove(10)
    #remmoving 2nd 10
    my_list.remove(10)
    #converting the list back to a tuple
    my_tuple = tuple(my_list)

    return my_tuple

print(my_tuple())

