#1.7 If...else...

#----------------------------------------

#IF is a logical condition with a following format
#Note: Result statements MUST have at least one white space at the beginning of the line
#      Programmers usually use 1 tab = 4 white spaces for each result statement

# if <Initial Statment>:
#   <Result Statements>

a = 3
b = 2
if a > b:
    print ("a is greater than b, since 3 > 2")   

#----------------------------------------

#Some IF statements have more than one coditions
#Python allows user to use ELIF for additional statements
#An IF statement can have multiple ELIF but only have one if
#IF has to be the first statement then ELIF

#elif <Initial Statment>:
#   <Result Statements>

age = 25
if age >=16 and age <= 18:
    print("teenager")
elif age >= 18:
    print("adult")

#----------------------------------------

#Since an if statement may have infinite possible results
#Python use ELSE to catches all conditions left
#ELSE only need result statement 

#else:
#   <Result Statement>

else:
    print("child")

#every IF need at least one <Result Statement>, you can use PASS in case you have an empty if statement to avoid error 
#For example:

if age > 24:
    pass

#----------------------------------------

#Nested IF
#One or more IF in an IF
#The outer IF will be executed first then the inside
