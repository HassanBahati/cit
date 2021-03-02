
'''
QUIZ
Write a variable called 'name' and set it to your name and print it out in the terminal
write a loop that prints out the number -1 to -10
Define a function called hello which prints out hello world in the terminal after calling it 
define a function called sum which takes two parameters (x,y) write a variable z inside which calcluates the sum and returns z
print out all odd numbers 1 to 100 using the modulo operator 
write an algorithm to detect prime numbers . hint isPrime()
'''

#Write a variable called 'name' and set it to your name and print it out in the terminal
name = 'Hassan Bahati Mukisa'
print(name)

#write a loop that prints out the number -1 to -10
i = -1
while i < 0:
    print(i)
    if i == -10:
        break
    i -= 1

#Define a function called hello which prints out hello world in the terminal after calling it 
def hello():
    return 'hello world'
print(hello())

#define a function called sum which takes two parameters (x,y) write a variable z inside which calcluates the sum and returns z
def sum(x, y):
    z = x + y
    return z
print(sum(2, 2))

#print out all odd numbers 1 to 100 using the modulo operator 

#write an algorithm to detect prime numbers . hint isPrime()
