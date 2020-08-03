#2.1 - Practices

#NOTE: from now on, all solutions are stored in seperated functions 

#----------------------------------------

#Question 0
#Create function question1, question2, question3, and questionMenu
#questionMenu will give three options for question 1, 2, and 3
#Once input received, it will call the question's function

#----------------------------------------

#Solution 0

print("2.1 - Functions Practice\n")

def question1():
    print("\nQuestion 1")
    yourName = input("Please enter your name: ")
    print ("Hi", yourName)
    doAgain = input("\nDo you want to do other questions(Y/N): ").lower()
    if (doAgain == "y"):
        practiceMenu()

def question2():
    print("\nQuestion 2")
    listOfName = list(range(0))
    names = ""
    
    while(names != "exit"):
        names = input("Please enter a name, input \"exit\" to stop: ").lower()
        listOfName.append(names)
    
    listOfName.pop()
    
    for x in listOfName:
        print("Hello ", x)
    
    doAgain = input("\nDo you want to do other questions(Y/N): ").lower()
    if (doAgain == "y"):
        practiceMenu()

def question3():
    print("\nQuestion 3: Chinnese Zodiac Calculator")
    birthYear = int(input("Please enter the year you want to know: "))
    birthYear %= 12
    if (birthYear == 0): print("Monkey")
    elif (birthYear == 1): print("Rooster")
    elif (birthYear == 2): print("Dog")
    elif (birthYear == 3): print("Pig")
    elif (birthYear == 4): print("Rat")
    elif (birthYear == 5): print("Ox")
    elif (birthYear == 6): print("Tiger")
    elif (birthYear == 7): print("Cat")
    elif (birthYear == 8): print("Dragon")
    elif (birthYear == 9): print("Snake")
    elif (birthYear == 10): print("Hourse")
    else: print("Goat")

    doAgain = input("\nDo you want to do other questions(Y/N): ").lower()
    if (doAgain == "y"):
        practiceMenu()

def practiceMenu():
    print("Question 1: Say Hi to a given person.")
    print("Question 2: Say Hi to a set of given people.")
    print("Question 3: Calculate user's Chinese Zodiac.")

    questionNumber = int(input("\nInput the question number you want to do (number only): "))
    if (questionNumber == 1): question1()
    elif (questionNumber == 2): question2()
    elif (questionNumber == 3): question3()
    else : 
        print("Invalid Input, please try again")
        practiceMenu()

practiceMenu()

#----------------------------------------

#Question 1
#In question1(), write a function that ask for a name
#The variable will receive input information from the user
#Then, the Computer will say "Hi + input name"
#Ask if the user want to do other questions
#If so, call the questionMenu at the end of question1

#----------------------------------------

#Question 2
#In question2(), promtp the user to input as many user as they want
#Input exit to stop
#The Computer will say Hi to every one of them but exit
#Ask if the user want to do other questions
#If so, call the questionMenu at the end of question2

#Hint: use list.append() to add a new item to the end of a list
#      use list.pop() to delete an element from a list

#----------------------------------------

#Question 3
#In question3(), Prompt the user to input a year
#Use algorithm to out the Chinese Zodiac
#Ask if the user want to do other questions
#If so, call the questionMenu at the end of question3

#In case you don't know about Chinese Zodiac
#http://theroyalgarden.co.uk/chinese-zodiac/

#Hint: Year 1 AD is the year of rooster

