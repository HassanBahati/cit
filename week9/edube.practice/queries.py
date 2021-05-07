#print(x) prints the keys while print(dit[x]) prints the values then when an index is added it prints only the indexed
dit={}
dit['1']=(3,4)
dit['2']=(4,5)
for x in dit.keys():
    print(dit[x][1], end='')

my_list=[1,2]
for v in range(2):
    my_list.insert(-1, my_list[v])
print(my_list)
