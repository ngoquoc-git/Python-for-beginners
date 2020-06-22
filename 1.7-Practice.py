#1.7 Practice

#----------------------------------------

#Question 1
#Add three random grades 0~100 for math, physics, and chemistry
#Find an average grade
#Convert average grade from 100 scale to A-F scale
#Prompt the computer to print out final grade using if statemnt

#Question 2
#Write a machine that giving changes less than $1 in quarters(25 cents), dimes(10 cents), nickles(5 cents), pennies(1 cent)
#For example: if the change is 79 cents, the change machine will give 3 quarters(75 cents), 4 pennies(4 cents)

#If you are confident, try upgrading your codes
#Upgrade 1: Input changes instead of initiating change using input("<text>")

#Upgrade 2: Given itemPrice is $79.29, input the amount you pay. Then, let the machine calculate changes in both bills and coins 

#----------------------------------------

#Solution 1
math = 87
physics =  92
chemistry = 90

averageGrade = (math + physics + chemistry) / 3

if averageGrade <= 100 and averageGrade > 89: print("Your grade is A")
elif averageGrade > 79 and averageGrade < 90: print("Your grade is B")
elif averageGrade > 69 and averageGrade < 80: print("Your grade is C")
elif averageGrade > 59 and averageGrade < 70: print("Your grade is D")
else: print("Your grade is F")