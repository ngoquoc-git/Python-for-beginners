#2.1 Functions

#----------------------------------------

#A function is a bunch of template codes to do a certain work when it is called
#A function contains data, parameters, and returned data
#A function has two parts: Function Implementation and Calling

#----------------------------------------

#Function Implimentation
#It holds functions codes

def displayName():
    print("Hello Wolrd!")

#----------------------------------------

#Function Calling
#You can call the function multiple times along your code when ever you need to

displayName()

#----------------------------------------

#Arguments or Parameters
#A argument is typically simmilar to a parameter

#A parameter is the variable which is listed in a function's name
#For example: displayName(name)     name is a parameter

#An argument is the value that a function receive when being called
#For example:   name = "John"
#               displayName(name)     the value of variable name which is "John" is an argument

def helloName(yourName):
    print ("Hello ", yourName)

name = input("Please enter your name: ")
helloName(name)

#A function can pass more than one parameter
def recSur(length, width):
    return length * width

a = 4
b = 3
surface = recSur(a,b)
print ("The area is ", surface)

#Arbitrary Argument
#Sometimes, there are multiple args need to be pass to a parameter
#We use a pointer as a parameter by adding "*" before the parameter's name
#Search from a TUPLE

def showCar(*car): 
    print (car[1])

showCar("Toyota", "BMW", "Honda")

#Parameter orders do not matter when you assign value to them
#We call it a keyword argument or kwargs

def showName(name1, name2, name3):
    print("Only name3 is display: ", name3)

showName(name3 = "Tom", name1 = "Tony", name2 = "Tim") 

#A "**" is used in case there are multiple keyword arguments
#Search from a DICT

def showId(**id):
    print("Name: ", id["name"])
    print("ID: ", id["numbers"])

showId(numbers = "0001", name = "David")

#Default Parameter Value
#Programmer can give parameters in their functions default value to avoid errors

def printSchool(school = "Cal State Long Beach"):
    print("I am studying at ", school)

mySchool = "Santa Ana College"

printSchool(mySchool)
printSchool()    

#Passing a list in functions

myDrink = ["Cognac", "Whiskey", "Volka"]

def showDrink(drink):
    for x in drink:
        print(x)

showDrink(myDrink)

#A function can eitrher ruten values or not
#The previous functions do not return any value
#Here is an example for a function with return value

def squareArea(side):
    return side * side

squareArea(4)

#Empty functions
#Some functions may be empty
#using "pass" to avoid unwanted errors

def empFct():
    pass

#Recussion
#To write a loop in a function, Python support recusion
#It is when a function calls itself 

def checkLoop():
    answer = input("Type \"y\" to loop, \"n\" to end: ")
    if (answer.lower() == "y"):
        checkLoop()

checkLoop()    

