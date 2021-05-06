i = 2 
while i >= 0:
    print('*')
    i-=2




tup1=(1,)
tup2=(1,)
tup=tup1+tup2
print(len(tup))

def func(x):
    global y
    y = x*x
    return y
func(2)
print(y)

rup=(2,4,6)
i=0
# for i in range(2,8,3):
#     print(i)


# print("The break instruction:")
# for i in range(1, 6):
#     if i == 3:
#         break
#     print("Inside the loop.", i)
# print("Outside the loop.")


# print("\nThe continue instruction:")
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print("Inside the loop.", i)
# print("Outside the loop.")
word = "Python"
for letter in word:
    print(letter, end="*")

text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")

text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")

num=[10,5,7,2,1]
num[0]=num[4]
print(num)

my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)

my_list = [10, 1, 8, 3, 5]
length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)

# # Read two numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))

# # Choose the larger number
# if number1 > number2:
#     print(number1)
# else:
#     print(number2)

# # # Print the result
# print("The larger number is:", larger_number)

