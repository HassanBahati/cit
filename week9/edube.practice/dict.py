#can contain any data type
#lists of ke value pairs
#no duplicate keys

heroes={
    "Superman": "Clarke Ken",
    "Batman"
: "Bruce Wayne"}
#length
print('length', len(heroes))

 #changing a value
heroes['Flash']='Barry Allen'
print(heroes) 

#printing list from a dict
print(list(heroes.items()))

#get lists and keys 
print(list(heroes.keys()))

#only values
print(list(heroes.values()))

#deleting froma  dictionary
del heroes['Flash']
#delete an item and return it
print(heroes.pop('Batman'))

print(list(heroes.items()))
print('--------------')
#cycle throgh dict
for k in heroes:
    print(k)