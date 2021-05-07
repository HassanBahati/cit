#anyting done to a list can happen with a tuplee except changing a value 

t1=(1,3.14,'Derrick')
print('length', len(t1))
print('1st', t1[0])
print('lst', t1[-1])
print('every other', t1[0:-1:2])
print('reverse', t1[::-1])

print(end='')


#all divisions with floats inclusive offer a float as a result 
x=2.0
y=4
print(y//x)

my_lst=[10,1,8,3,5]
total=0
for i in range(len(my_lst)):
    total+=my_lst[i]
print(total)

my_lst=[10,1,8,3,5]
total=0
for i in my_lst:
    total+=i
print(total)

