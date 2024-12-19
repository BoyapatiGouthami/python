#AND
a=10
b=20
c=30
#result=(a>b)and(b>c):
#print(result)

#OR
a = 20
b = 30
c = 10
if c < b or c > b :
    print("Any one condition is true")

#NOT
a = 50
b = 40
c = 10
if not a == c :
    print("a is not equal to c")

#IF
fruit = "Orange"
if fruit == "apple":
    print("It's an apple!")
else:
    print("It's not an apple.")

#ELSE
age = 15
if age >= 18 :
    print("you are eligible to Vote")
else :
    print("you are not eligible to Vote")

#ELIF
marks=85
if marks>=90:
    print("Distintation")
elif marks>50 and marks<90 :
    print("avg")
else:
    print("fail")

#While
count = 50
while count <= 50:
    print(f" Count is: {count}")
    count += 1  # Increment the count by 1
print("Loop finished!")

#For
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(f" Current number is: {number}")

#IN
fruits = ['apple', 'grapes', 'banana', 'mango']
if 'kiwi' in fruits :
    print("kiwi is present")
else :
    print("not present")

#Try
a = 20
b = 0
try :
    c = a / b
    print("div : ",c)
except Exception as e:
    print("e")
    print("Div by 0 NOT-OK in python")

#Except
a = 20
b = 0
try :
    c = a / b
    print("div : ",c)
except Exception as e:
    print("e")
    print("Div by 0 NOT-OK in python")

#return
def square(num):
    return num * num
result = square(5)
print(result)  #output: 25

def even(num):
    if num % 2 == 0:
        return True
    return False
print(even(4))   #output: true
print(even(7))   #output:false

#import #as
import numpy as np
array = np.array([1,2,3,4])
print(array)  #output: [1 2 3 4]

#class
class dog:
    attr1="mammal"
    attr2="dog"
    def fun(self):
        print("This is a",self.attr1)
        print("This is a",self.attr2)
bark=dog()
print(bark.attr1)
bark.fun()
#output: mammal
        # this is a mammal
        # this ia a dog

#from
from math import sqrt
result =sqrt(25)
print("square root of 25 is",result)  #output: square root of 25 is 5.0


#True
x=20
if x>15:
    print("True")
else:
    print("False")  #output: True

#false
x=6
if x>10:
    print("True")
else:
    print("False")   #output: False

#None
value= 10
if value is None:
    print("The value is none")
else:
    print("The value is not none") #output: the value is not none

value = None
if value is None:
    print("the value is none")
else:
    print("the value is not none")

#is
a=10
b=10
print(a is b) #output: true

a=10
b=20
print(a is b) #output: False

#lambda
add=lambda x:x+10
print(add(5)) #output: 15

# adding two numbers to the function
add=lambda x,y:x+y
print(add(5,4))  #output: 9

#global
c=2
def add():
    global c
    c=c+2
    print(c)
add() #output: 4

#nonlocal
x=5
def name():
    x=10
    print("Non-local x:",x)
name()
print("global x:",x)  #output: Non-local x: 10 global x: 5



