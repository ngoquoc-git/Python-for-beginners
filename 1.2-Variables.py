#1.2 Variables in Python

#----------------------------------------

#Variable is used to store data values
#Unlike other language, Python does not need developer to declare the variable types
#Variable type can be flexibly changed depends on user input

a = 5       #declare variable a as an integer 
print (a)

a = "Tom"   #declare the variable a above as a string
print (a)

#Note: "Tom" is the same thing as 'Tom'

#----------------------------------------

#Naming Variable

#Variable names can be lowercase, uppercase, number, and underscore

firstvar = 0
first_var = 0
first_var_ = 0
_first_var = 0
FirstVar = 0
FIRSTVAR = 0
first1var = 0
firstvar1 = 0

#Variable cannot contain hyphen, space and number at the beginning

#first-var = 0
#first var = 0
#1firstvar = 0

#----------------------------------------

#Playing with Variable in Python

#Multiple variable has the same value can be added in one line

a = b = c = 3

#The "+" operator can be used to add one variable with another
#The type of variables have to be the same
#For example: number + number and string + string
#A number cannot combien with a string

a = 3
b = 2
c = a + b
print (c)

#The "+" operator can be used in "print" command

b = 2
print(a + b)