#allow to perform an actiona  a set number of times

#printing all items in range
for x in range(0,10):
    print(x, "", end='')
print()

#cylce througha  list 
l4=[1,3,'Derrick']
for x in l4:
    print(x)

#cycle through a defined list
for x in [2,4,6]:
    print(x  )

print('------------------------------')
#iterators-help to cycle trhough values, rinting one by one 
l5=[6,9,12]
itr=iter(l5)
print(next(itr))
print(next(itr))
print(next(itr))

#range
print(list(range(0,10,2)))