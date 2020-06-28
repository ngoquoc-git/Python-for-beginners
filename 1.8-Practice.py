#1.8 Practice

#----------------------------------------

#Question 1
#Prompt the computer to print from 1 to 10 using loop
#Ask user if he/she wants to do it again using loop

#Question 2
#Write a rock-paper-scissor game
#The winning condition is either the player or the computer win 3 times first
#Hint: import random

#----------------------------------------

#Solution 1
answers = 'y'
while answers == 'y':
    for i in range(1,11):
        print (i)
        i += 1
    answers = input("Do you want to do it again (y/n): ").lower()

#Solution 2
import random

playerScore = 0
computerScore = 0
print("1 is ROCK, 2 is PAPER, or 3 is SCISSOR")
while playerScore != 3 or computerScore!= 3:
    print ("\nGame Score is now ", playerScore, " Player, ", computerScore) #Scores Tracker  
    
    playerChoice = input("PLease choose an option: ")       #Get inputs from the user
    computerChoice = random.randrange(1,3)                  #Generate a random decision for the computer
    
    if playerChoice == 1:                                   #Convert player's decisions      
        playerDecision = "ROCK"
    elif playerChoice == 2:
        playerDecision = "PAPER"
    elif playerChoice == 3:
        playerDecision = "SCISSOR"
    else:
        playerChoice = "INVALID ENTRY"

