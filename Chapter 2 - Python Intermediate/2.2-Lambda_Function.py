#2.2 Lambda Function

#----------------------------------------

#Lambda is an anonymous fucntion
#Lambda function is used in small funtions for a short period period time
#Lambda functions can be used in a variable or a function

#A lambda function can only have one expression with multiple arguments

#Lamnbda with 1 argument
lambda1 = lambda x: x*4
print (lambda1(3))

#Lambda with more than one arguments
lambda2 = lambda a, b, c: (a * b) + c
print(lambda2(2, 6, 3))

#----------------------------------------

#Lambda function in a function

def recSqr(width):
    return lambda height : width * height

width1 = 4
height1 = 7

myRec = recSqr(width1)
print (myRec(height1))


