from mymodule.helper_utils import square

print("Basic Program\n")

print("Hello world") #Display a message

#Get user input and display a message
my_name = input("What is your name: ")
print("Hello "+ str(my_name))

#Alternative way to format a string
print("Hello %s" % my_name)


print("\nVariables\n")

i = 120
print(f"Variable i has the value {i}")

f = 1.638292
print(f"Variable i has the value {f} and its type is {type(f)}")

b = True
print(f"Variable b has the value {b}")

n = None
print(f"Variable n has the value of {n}")

#Tuple

c = (10,20,10)
print(f"c[0] has the value {c[0]} and is of type {type(c)}")

#List
l = ["Ana","Tom","John"]
l = [10,20,30]
print(f"l[0] has the value {l[0]} and is of {type(l)}")

#set variables

s = set()
s.add(1)
s.add(3)
s.add(6)
s.add(5)
print(s)

#Dictionary

grades = {"Tom": "A", "Mark": "B-"}
grades["Tom"]
grades["Anna"] = "F"
print(grades)

#create an empty Dictionary
my_dictionary = dict()
print(my_dictionary)

print("\nConditionals\n")

x = 10
if(x>0):
    print("The number x is positive")
elif(x<0):
    print("The number is negative")
else:
    print("The number is zero")


print("\nLoops\n")

for i in range(5):
    print(i)

for i_idx, i_value in enumerate(range(2,10)):
    print(f"{i_idx} - {i_value}")

print("\nFunctions\n")

def is_even(x):
    if (x % 2) == 0:
        return True
    else:
        return False

print(f"Expected False and got {is_even(-15)}")

print("\nClasses\n")

class Book:
    def __init__(self, title="Software Engineering", isbn=""):
        slelf.title = title
        self.isbn = isbn
    def printBook(self):
        print(self.title + ", "+ self.isbn)

print("\nDefining modules\n")
print("mymodule/helper_utils")

print("\nUse a module\n")

print(square(100))
