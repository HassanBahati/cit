#print(x) prints the keys while print(dit[x]) prints the values then when an index is added it prints only the indexed
dit={}
dit['1']=(3,4)
dit['2']=(4,5)
for x in dit.keys():
    print(dit[x][1], end='')

#lists
my_list=[1,2]
for v in range(2):
    my_list.insert(-1, my_list[v])
print(my_list)

#
my_list=[x*x for x in range(5)]
def func(lst):
    del lst[lst[2]]
    return lst
print(func(my_list))

#modulo


print(1^0)

my_list=[0 for i in range(1,3)]
print(my_list)

i=2
while i >=0:
    print(i)
    i-=2