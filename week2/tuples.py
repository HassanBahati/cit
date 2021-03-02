'''
TUPLES
tuples are ordered and unchangeable collections 
tuples allow dupliate values
'''
a_tuple = (1,2,3,4,5)

a_tuple = list(a_tuple)
#adding an item to the tuple
a_tuple.append(6)
a_tuple = tuple(a_tuple)

print(a_tuple)
#printing the data type 
print(type(a_tuple))

x_tuple = (10,11,12,13,14,15)
y_tuple = x_tuple[:2]
z_tuple = x_tuple[2:4]
#to print out 10 and 11
print(y_tuple)
#to print out 12 and 13
print(z_tuple)

single_tuple = (90,)
print(single_tuple)