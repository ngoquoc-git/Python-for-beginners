#1.6 Python Operators

#----------------------------------------

#Python uses operators to perform connections between variables and value
#There are 7 kinds of operators: Arithmetic Operators
#                                Assignment Operators
#                                Comparison Operators
#                                Logical Operators
#                                Identity Operators
#                                Membership Operators
#                                Bitwise Operators

#----------------------------------------

#Arithmetic Operators
print("Arithmetic Operators:")

#These operators perform common mathematical operations
# Addition:         +       x + y       
print("10 + 3 =", 10 + 3)
# Subtraction:      -       x - y       
print("10 - 3 = ", 10 - 3)
# Multiplication:   *       x * y      
print("10 * 3 = ", 10 * 3)
# Division:         /       x / y       
print("10 / 3 =", 10 / 3)
# Modulus:          %       x % y       
print("10 % 3 =", 10 % 3)
# Exponentiation:   **      x**y        
print("10**3 =", 10**3)
# Floor Division:   //      x//y
print("10//3 =", 10//3)

#----------------------------------------

#Comparison Operators
print("\nComparison Operators:")

#These operators are used to compare two values
a = 1 
b = 3
print("Since a = 1 and b = 3")
#Equal              ==      a==b
print("a==b is ", a==b)
#Not equal          !=      a!=b
print("a!=b is ", a!=b)
#Greater than       >       a > b
print("a > b is ", a > b)
#Less than          <       a < b
print("a < b is ", a < b)
#Greater or equal   >=      a >= b
print("a >= b is ", a >= b)
#Less or equal      <=      a <= b
print("a <= b is ", a <= b)

#----------------------------------------

#Logical Operators
print("\nLogical Operators:")

#Logical operators are conditional operator
a = 4
# and   Return true if all statements are true          a < 3 and a < 5
print ("Since a = 4, a < 3 and a < 5 is ", a < 3 and a < 5)
# or    Return true if one of the statements is true    a < 3 or a < 5
print ("Since a = 4, a < 3 or a < 5 is ", a < 3 or a < 5)
# not   Return false if the statement is false          not(a < 3 and a < 5)
print ("Since a = 4, not(a < 3 and a < 5) is ", not(a < 3 and a < 5))

#----------------------------------------

#Identity Operators
print("\nIdentity Operators:")

#Compare if two variables are equal or have the same object
a = [1, 2]
b = [0, 5]
c = a
# is        Return true if both variables have the same object          a is c
print("a is c is ", a is c)
print("a is b is ", a is b)
# is not    Return true if both variables do not have the same object   a is not b
print("a is not b is ", a is not b)

#----------------------------------------

#Membership Operators
print("\nMembership Operators:")

#Membership operators are used to test if a sequence is presented in an object
a = [1, 2]

# in        Return true if a sequence with the specified value is present in the object         a is c
print("1 is in a is ", 1 in a)
# not in    Return true if a sequence with the specified value is not present in the object     a is not b
print("1 is not in a is ", 1 not in a)


#----------------------------------------

#Bitwise Operators
print("Bitwise Operators: ")

# &  	AND 	Sets each bit to 1 if both bits are 1
# | 	OR 	Sets each bit to 1 if one of two bits is 1
# ^ 	XOR 	Sets each bit to 1 if only one of two bits is 1
# ~  	NOT 	Inverts all the bits
# << 	Zero fill left shift 	Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >> 	Signed right shift 	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

#----------------------------------------

#Assignment Opoerators
print("\nAssignment Operators:")

#These operators assign value to variables
# =     a = 4
a = 4
print("a = ", a)
# +=    a = a+=4    a = a + 4
a+=4
print("a += 4 is ", a)
# -=    a = a-=4    a = a - 4
a-=4
print("a -= 4 is ", a)
# *=    a = a*=4    a = a * 4
a*=4
print("a *= 4 is ", a)
# /=    a = a/=4    a = a / 4
a/=4
print("a /= 4 is ", a)
# %=    a = a%=4    a = a % 4
a%=4
print("a %= 4 is ", a)
# //=   b//=5   b = b//5
b = 7
b//=5
print("b//=5 is ", b)
# **=   c**=3    c = c**3
c = 2
c**=3
print("c**=3 is ", c)
# &=    d&=3    d = d&3
d = 7
d&=3
print("d&=3 is ", d)
# |=    e|=3    e = e|3
e = 7
e|=3
print("e|=3 is ", e)
# ^=    f^=3    f = f^3
f = 5
f^=3
print("f^=3 is ", f)
# >>=    g>>==3    g = g>>3
g = 5
g>>=3
print("g>>=3 is ", g)
# <<=    h<<==3    h = h<<3
h = 5
h<<=3
print("h<<=3 is ", h)