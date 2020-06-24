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
print("Question 1 - Solution")

math = 87
physics =  92
chemistry = 90

averageGrade = (math + physics + chemistry) / 3

if averageGrade <= 100 and averageGrade > 89: print("Your grade is A")
elif averageGrade > 79 and averageGrade < 90: print("Your grade is B")
elif averageGrade > 69 and averageGrade < 80: print("Your grade is C")
elif averageGrade > 59 and averageGrade < 70: print("Your grade is D")
else: print("Your grade is F")

#Solution 2
print("\n\nQuestion 2 - Solution")

fullPrice = 79.29

print("The item price is $", fullPrice, ".")
paid = float(input("Enter paid amount: "))  #all the inputs are in strings, so you have to convert it to a number type
change = paid - fullPrice                   #make the result 2 decimal places

if change < 0:                              #check if user pay enough money
    print("Not enough money, please add more funds")
elif change == 0:                           
    print("You paid an exact amount, there is no change")
else:
    change*=100                             #multiply by 100 to get rid of the two decimal places
    bills =  change // 100
    coins = change % 100
    oneHundred = fifty = twenty = ten = five = two = one = quarters = dimes = nickles = pennies = 0
    
    if bills > 100:                         #counting $100 bills
        oneHundred = int(bills // 100)
        bills -= (oneHundred * 100)
    
    if bills > 50:                          #counting $50 bills
        fifty = int(bills // 50)
        bills -= (fifty * 50)

    if bills > 20:                          #counting $20 bills    
        twenty = int(bills // 20)
        bills -= (twenty * 20)
    
    if bills > 10:                          #counting $10 bills
        ten = int(bills // 10)
        bills -= (ten *10)
    
    if bills > 5:                           #counting $5 bills
        five = int(bills // 5)
        bills -= (five * 5)
    
    if bills > 2:                           #counting $2 bills
        two = (bills // 2)
        bills -= (two * 2)
    
    if bills > 1:                           #counting $1 bills
        one = int(bills)

    if coins > 25:                          #counting 25 cents
        quarters = int(coins // 25)
        coins -= (quarters * 25)
    
    if coins > 10:                          #counting 10 cents
        dimes = int(coins // 10)
        coins -= (dimes * 10)

    if coins > 5:                          #counting 5 cents
        nickles = int(coins // 5)
        coins -= (nickles * 25)

    if coins > 1:                          #counting 1 cent
        pennies = int(coins)

    print ("\nYour change is $", (round(paid - fullPrice, 2)))
    print ("You will receive:")
    print (oneHundred, "bill(s) $100    ", fifty, "bill(s) $50    ", twenty, "bill(s) $20")
    print (ten, "bill(s) $10     ", five, "bill(s) $5     ", two, "bill(s) $2    ", one, "bill(s) $1")
    print (quarters, "quarter(s)      ", dimes, "dime(s)        ", nickles, "nickle(s)     ", pennies, "penny(s)")