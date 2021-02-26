print('hello world')

#indenting specifies a block of code
if 5 > 2:
    print('Five is greater than two')

#variables
x = 5
y = 'John'
print(x)
print(y)

x = 'awesome'
print('pythton is ' + x)

y = 'python is'
print(y + x)

x = 5
y = 10
print(x + y)
#complex data type is a nmuber with a j as the imaginary part
z = 1j
print(type(z))
'''
float data type are numbers with decimals or
a number with e to mean power of 10
'''
m = 35e5
n = 40.64
print(type(m))
print(type(n))

#python casting - specifying the data type
#int() rounds off to decimals to the previous whole number
x = 5
print(int(x))
print(str(x))
print(float(x))

a = 'Hello, World'
print(a[1])
print(a[2:4])

#METHODS IN PYTHON -strip, len, lower,upper, replace
#strip() removes white spaces from beginning or end
h = '   hello, world   '
print(a.strip())

#len returns length of string 
b = 'Hello world'
print(len(b))

#lower makes string lowercase
c = 'BAHATI'
print(c.lower())

#upper makes a string uppercase
d = 'bahati'
print(d.upper())

#replace takes in the word you want to replace and the new word
f = 'good, morning'
print(f.replace('morning', 'afternoon'))

#split breaks a string into two
g = 'Hello, World'
print(a.split(','))

#input enables to take data from user through cmd
print('Enter your name:')
#x = input()
#print('Hello, ' + x)

#prints the result of the oopposite of the operation being true 
x = 4
print(not(x < 5))

#lists - ordered and changeable ---written in square brackets
thislist = ['apple', 'banana', 'cherry']
print(thislist)

#changing the 2nd item in a list
thislist[1] = 'blackcurrant'
print(thislist)

'''
list() constructor makes a list
append() contructor adds an item to the list
remove() constructor removes an item from the list 
'''

thislist = list(('mangoes', 'oranges', 'jackfruit'))
print(thislist)

thislist = list(('mangoes', 'oranges', 'jackfruit'))
thislist.append('damson')
print(thislist)

thislist = list(('mangoes', 'oranges', 'jackfruit'))
thislist.remove('mangoes')
print(thislist)

#len() method returns the number of items in a list
thislist = list(('mangoes', 'oranges', 'jackfruit'))
print(len(thislist))

'''
LIST METHODS
append() - adds an element to a list
clear() - removes all the elements from the list
copy() - returns a copy of the list
count() - returns the number of elements with the specified value
extend() - adds the element of a list (or any iterable), to the end of the current list
index() - returns the index of the first element with the specified value
insert() - addds an element at specified position
pop() - removes the element at the specified position
remove() - removes the first element with the specified value
sort() - sorts the list
'''

#tuple - ordered and uncheageable -- written in parentheses
thistuple = ('apple', 'banana', 'cherry')
print(thistuple)

#return element in position 1
print(thistuple[1])

#tuple() constructor makes a tuple
#len() function returns the length of the tuple

thistuple = tuple(('apples', 'bananas', ' cherry'))
print(thistuple)
#printing the length of the tuple
print(len(thistuple))

#set - unordered and unindexed -- written with curly braces
thisset = {'app', 'ban', 'cher'}
print(thisset)

'''
set() constructor makes a set
add() method adds an item
remove() removes an item from the set
'''

thisset = set(('app', 'ban', 'cher'))
print(thisset)

#adding an item
thisset.add('damson')
print(thisset)

#removing an item
thisset.remove('ban')
print(thisset)

#length of set
print(len(thisset))

'''
dictionary - unordered, changeable and indexed
--written with curly braces and have keys and values 
'''

thisdict = {
    'apple': 'green',
    'banana': 'yellow',
    'cherry': 'red'
    }
print(thisdict)

#changing the value of a key in a dict
thisdict['apple'] = 'red'
print(thisdict)

#dict() constructor makes a dictionarry
thisdict = dict(gender='male', nationality='ugandan', occupation='programmer')
'''
key words are not strings
equals operator rather than colon for assignment 
'''
print(thisdict)

#adding an item
thisdict['damson'] = 'kenyan'
print(thisdict)

#removing an item
del(thisdict['gender'])
print(thisdict)

#length of a dict
print(len(thisdict))

'''
PYTHON CONDITIONS AND IF STATEMENTS
equals: a == b
not equal: a!= b
less than or equal to: a<= b
greater than: a>b
'''

#if statement is written with key word if

a = 33
b = 200
if b > a:
    print('b is greater than a ')

#python uses indention , other languages use braces for same purpose

'''
elif keyword is pythons way of saying if the previous condition is not true , then do this condition
else keyword catches anything which isnt caught by preceding conditions 
'''
a = 33
b = 33
if b > a:
    print('b is greater than a')
elif a < b:
    print('a is less than b')
else:
    print('a is equal to b')

'''
PYTHON LOOPS
while loop - can loop and execute a set of statements as long as the condition is true
'''
i = 1
while i < 6:
    print(i)
    i += 2
'''
if i is not given an increament , the loop prints 1 forever
break statement stops the loop even if the while condition is true
'''

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

#continue statement we stop the current iteration and continue with the next

i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)

'''
for loop used for iterating a sequence (list, tuple, or string)
does not require an indexing variable to set beforehand, as for the command itself allows for thiss
'''

fruits = ['apples', 'banana', 'cherry']
for x in fruits:
    print(x)

#with break statement we can stop the loop before it loops through all items

fruits = ['apples', 'banana', 'cherry']
for x in fruits:
    if x == 'banana':
        break
    print(x)

#continue statement we can stop the current iteration of the loop and continue with the next
#when you rach what i have specified , skip it and move to the next etc
fruits = ['apples', 'banana', 'cherry']
for x in fruits:
    if x == 'banana':
        continue
    print(x)

'''
range() function loops through by a specifed number of times
starts from 0 by default , increments by 1 (default)
'''
for x in range(6):
    print(x)




























































