#1.3-Date Types in Python

#----------------------------------------

#Variables in Python can store different data type

#Text Type
a = "name"                  #str
#A multiline string is wrap in a triple quotation marks
a1 = """This is an
example of a 
multiline string"""

#Numeric Types
b = 1                       #int
c = 2.2                     #float
d = 1j                      #complex

#Sequence Types
e = ["a", "b", "c"]         #list
f = (1, 2, 3)               #tuple
g = range(4)                #range

#Mapping Type
h = {"val": 1,"add": 22}    #dict

#Set Types
i = {"ab", "cd", "ef"}      #set
g = frozenset({0, 1, 2})    #frozenset

#Boolean Type
k = True                    #boolean

#Binary Types
l = b"Hello"                #bytes
m = bytearray(4)            #bytearray
n = memoryview(bytes(3))    #memoryview

#Print values
print(a)
print(a1)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(g)
print(k)
print(l)
print(m)
print(n)

#Print date type
print(type(a))
print(type(a1))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(g))
print(type(k))
print(type(l))
print(type(m))
print(type(n))

#----------------------------------------

#Type Conversion

#Data of the same type can be converted between each other
x = float(b)
y = int(c)

print(x)
print(type(x))

print(y)
print(type(y))