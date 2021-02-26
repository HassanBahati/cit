'''
function is block of code which only runs when it is called
'''

def my_function():
    print('hello from a function')
print(my_function())

def new_function(fname):
    print(fname + 'Refsnes')
new_function('linux')

def my_function(country = 'Uganda'):
    print('I am from ' + country)
my_function()
my_function('Sweden')

def my_function(x):
    return 5 * x
print(my_function(3))

x = lambda a, b, c : a + b + c
print(x(1,2,3))
