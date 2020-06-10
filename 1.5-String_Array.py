#1.5 String Array

#----------------------------------------

#Python does not have character type
#Therefore, string is used as a character array
string1 = "This is a string"

print(string1[2])       #Access the 2nd element of array string1 
print(string1[4:8])     #Access element 4th-7th of string1 from the beginning
print(string1[-8:-4])   #Access element 5th-8th of string1 from the end

#len() function is used to get the length of the string
print(len(string1))

#Check string
a1 = "a str" in string1
print(a1)

a2 = "a str" not in string1
print(a2)

#Use format method to combine strings and numbers
#argument will be passed in the placeholder "{}"
age = 25
zip = 92708

statement1 = "I am {} years old"
print(statement1.format(age))

statement2 = "I am {0} years old and live at {1}, California"
print(statement2.format(age, zip))

#----------------------------------------

#Built-in string methods
#To get rid of unecessary blank spaces at the beginninf and the end of a string
string2 = "  blank spaces will be deleted  "
print(string2.strip())

#To change string to upper case
print(string2.upper())

#To change string to lower case
print(string2.lower())

#To replace a string with another
print(string2.replace("b", "p"))

#To split string
print(string2.split(" "))   #" " is the instance separator

