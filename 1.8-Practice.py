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
print("Question 1\n")
answers = 'y'
while answers == 'y':
    for i in range(1,11):
        print (i)
        i += 1
    answers = input("Do you want to do it again (y/n): ").lower()

#Solution 2
import random

loop = 'y'
playerScore = computerScore = 0
playerChoice = computerChoice =0
playerDecision = computerDecision = 'INVALID ENTRY'
print("\nQuestion 2\n")

while loop == 'y':                                              #play multiple games
    playerScore = computerScore = 0
    print ("\nGame Score is now ", playerScore, " Player, ", computerScore, " Computer") #Scores Tracker
    while playerScore < 3 and computerScore < 3:  
        print("\n1 is ROCK, 2 is PAPER, or 3 is SCISSOR")

        playerChoice = int(input("PLease choose an option: "))  #Get inputs from the user
        computerChoice = random.randrange(1,4)                  #Generate a random decision for the computer
        
        while playerDecision == "INVALID ENTRY":
            if playerChoice == 1:                                   #Convert player's decisions      
                playerDecision = "ROCK"
            elif playerChoice == 2:
                playerDecision = "PAPER"
            elif playerChoice == 3:
                playerDecision = "SCISSOR"
            else:
                playerDecision = "INVALID ENTRY"

        if computerChoice == 1:                                   #Convert computer's decisions      
            computerDecision = "ROCK"
        elif computerChoice == 2:
            computerDecision = "PAPER"
        else:
            computerDecision = "SCISSOR"

        print ("\nPlayer chose ", playerDecision)
        print ("Computer chose ", computerDecision)

        if (computerChoice % 3) + 1 == playerChoice:              #Win - Lose conditions
            print("Player wins")
            playerScore += 1
        elif (playerChoice % 3) + 1 == computerChoice:
            print("Computer wins")
            computerScore += 1
        else: print ("Draw")
        print ("\nGame Score is now ", playerScore, " Player, ", computerScore, " Computer") #Scores Tracker
    if playerScore == 3:
        print("Player wins with 3 scores")
    else:
        print("Computer wins with 3 scores")
    loop = input("\nDo you want to play another game: ").lower()