'''
x = "chapcabra"
while True:
    i = input("Enter a word")
    if x == i:
        print("You have succesfully left the loop")
        break
    else:continue
'''
    '''
user_word = input("Enter a word:")
user_word = user_word.upper()
for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    else: break
'''

i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)
