#Random Number Guessing Game
#4/27/2021
#CTI-110 P5HW1 - Random Number
#Madelyn Perry
#
import main_menu
option= int(input())
if option ==2:
    exit()
elif option == 1:
    import random

def main():
    rand_num = random.randint(1, 100)
    guess = int(input("Enter a number from 1 and 100: "))
    count = 0
    while rand_num != "guess":
        count = count + 1
        print()
        if guess < rand_num:
            print ("Too low, try again.")
            guess = int(input("Enter a number from 1 and 100: "))
        elif guess > rand_num:
            print ("Too high, try again.")
            guess = int(input("Enter a number from 1 and 100: "))
        else:
            print ("Congratulations!!!")
            print("Number of entries: ", count)
            choice = int(input("Do you want to play again? 1 = Yes, 2 = No: "))
            if choice ==1:
                print(main())
            else:
                choice ==2
                exit()
                
   
            

main()

#START
#Program is a number guessing game
#IMPORT main_menu.py
#main_menu contains menu screen with two options:
# 1 --> Play Game or 2--> Exit
#IF the user enters 1, program will start
#ELIF the user enters 2, program will terminate
#ENDIF
#IMPORT random
#rand_num --> a random number between 1 and 100
#PRINT Enter a number from 1 and 100:
#IF the user enters number lower than random number
#THEN PRINT Too low, try again.
#PRINT Enter a number from 1 and 100:
#ENDIF
#IF the user enters a number higher than random number
#THEN PRINT Too high, try again.
#PRINT Enter a number from 1 and 100:
#ENDIF
#IF the user enters the correct number
#THEN PRINT Congratulations!!!
#PRINT Number of entries:, count
#ENDIF
#Program asks the user if they want to play again
#PRINT Do you want to play again? 1 = Yes 2 = No:
#IF the user enters 1,
#THEN the function will start over again with new random number
#ENDIF
#If the user enters 2
#THEN program will terminate
#ENDIF
#Program only termintates if the user enters 2
#END
