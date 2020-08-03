#1.8 Loops

#----------------------------------------

#Python let users use LOOP for statements that need to be executed infinite times till it reach its condition
#There are two kinds of loops are WHILE loop, and FOR loop

#----------------------------------------

#WHILE loop
#While loop will execute the <result statements> until the condition is still true
print ("Test WHILE Loop")
answer = 'y'
while answer == 'y':
    answer = input("Do you want to continue(y/n): ")    #Use input() to receive answers from the user 
    answer = answer.lower()                             #Turn all answer to lowercase

#----------------------------------------

#FOR loop
#FOR loop is used to read a specific sequence 
print("\nTest FOR Loops")
for i in range (6):
    print (i)
    i+=1

names = ["Amy", "Taylor", "Kevin"]
for x in names:
    print (x)

aString = "strawberry"
for n in aString:
    print (n)

#Nested Loop
#A loop inside a loop
#The inner loop will be read first than the outer loop
#The inner loop will be executed again, everytime the outer loop is executed
print("\nTest nested for loop")
cars = [["Toyota", 2009],["Honda", 2015],["Porsche", 2020]]
for i in cars:
    for n in i:
        print (n, end = " ")
    print()

#----------------------------------------

#Statements in loops
#BREAK statement
#The BREAK statement can stop the loop at any time even if the given statement is still true
print ("\nTest BREAK Statement")
a = 5
while a > 0:
    print (a)
    break

#CONTINUE statement
#CONTINUE statement is used to skip a current loop
print("\nTest CONTINUE Statement")
while a > 0:
    a-=1
    if a == 2:
        continue
    print (a)

#ELSE statement
#It works like in IF statement to run when the conditions are not true
print ("\nTest ELSE statement")
while a > 0:
    print (a)
else:
    print ("a is not larger than 0 any more")  

#----------------------------------------

#RANGE() function
#RANGE is used to execute the statements in a number of times
#By default, all range numbers start from 0 and increase by 1 everytime

#RANGE(<index number>)
print("\nTest range(<index>)")
for i in range(5):              #it wont count 5, from 0 to 4
    print (i)
    i+=1

#RANGE(<Starting point>,<Ending point>)
print("\nTest range(<strating point>,<ending point>)")
for i in range(2, 8):            #count from 2 to 7
    print (i)
    i+=1

#RANGE(<starting point>,<ending point>,<increment>)
print("\nTest range(<starting point>,<ending point>,<increment>)")
for i in range(5, 26, 5):        #count 5 to 25, add 5 at a time
    print (i)

