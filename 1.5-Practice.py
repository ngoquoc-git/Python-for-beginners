#1.5 String Array Practice

#----------------------------------------

#Question 1
#Declare day, month, and year in integer
#Create a string format day## month## year#### 
#Print today's date using format
#Check the length of the string 
#Turn the string to upper case
#Split the string into 3 parts day, month, and year

#Question 2
#Introducing youself using special characters in your introduction

#----------------------------------------

#Solution 1
day = 10
month = "June"
year = 2020
today = "day{0} month{1} year{2}"

print(today.format(day, month, year))
print(len(today.format(day, month, year)))
print(today.format(day, month, year).upper())
print(today.format(day, month, year).split(" "))

#Solution 2