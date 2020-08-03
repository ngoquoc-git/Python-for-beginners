#1.6 Python Operators Practice

#----------------------------------------

#Question 1
#Make a multiplication chart using only 2 variables
#Hint: using assignment operators and 2 for-loop to do the problem
# for i in range (range_number):
#   *statement

#----------------------------------------

#Solution 1
x = 1
y = 1
print("The multiplication chart:")
for i in range (9):
    print("\n", i + 1, "chart")
    for n in range(11):
        y = n * x
        n+=1
        print(n, " * ", x , " = ", y)
    x+=1
    i+=1


