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