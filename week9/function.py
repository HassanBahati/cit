#we wwill be trying out some piece of test code here

#define variable
Joseph = -34
print(abs(Joseph))

print('---------------------------------')

#all function 
all({'*', ','})
print(all({'*'})) #iteratable is been able to access through an item from index to the rear

print('---------------------------------')

#binary function
bin(7)
print(bin(7))

print('---------------------------------')

#bool function
bool(0.5)
print(bool(0.5)) #ask to check if 0.5 is a float 
print(bool(7))

print('---------------------------------')

#character function
chr(65)

print(chr(65), chr(97))
print('---------------------------------')
#class
class Hughey:
    def say_hi(self):
        print('Hi CIT students')
    # define a variable 
Hughey.say_hi = classmethod(Hughey.say_hi)

#calling function
Hughey.say_hi()

print('---------------------------------')
print('---------------------------------')

class Da_Shone:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
    @classmethod
    def Birthyear(cls, name, year):
        return cls(name, date.today().year-year)
    
    @staticmethod
    def Adult(age):
        return age > 18

    CIT_student_1 = Da_Shone('freddrich', 46)
    CIT_student_2 = Da_Shone('samuel', 12)

    CIT_student_1 = Da_Shone('freddrich', 1975)