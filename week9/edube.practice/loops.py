#while loop
#executes once operation is true
w1=1
while w1<5:
    print(w1)
    w1+=1

#to print even numbers
#break-stop loopoing   
w2=0
while w2 <= 20:
    if w2 % 2 == 0:
        print(w2)
    elif w2 == 9:
        break
    else:
        w2+= 1
        continue
    w2 += 1

#  looping through lists
l4=[1,3,3.14,"Derrick"]
while len(l4):
    print(l4.pop(0))

#infinity loop priting one star every line
i=0
while i<i+2:
    i+=1
    print('*')
else:
    print('*')