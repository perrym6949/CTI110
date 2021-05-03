#Math Quiz Game
#4/29/2021
#CTI-110 P5HW2 - Math Quiz
#Madelyn Perry
#
print("Welcome to Math Quiz")
print()
print()
#-------------------------------------------------------------------#
import random

def quiz_add():
    count = 0
    random_n = random.randint(0,100)
    rand_n = random.randint(0,100)
    answer1 = random_n + rand_n
    while ans !=1:
     count = count + 1
     print(" ",random_n)
     print("+", rand_n)
     print("Enter answer.")
     user_ans = int(input())
     if user_ans > answer1:
       print("Sorry, guess is too high.")
       print("Try again.")
     elif user_ans < answer1:
       print("Sorry, guess is too low.")
       print("Try again.")
       print()
     else:
       user_ans == answer1
       print("Congratulations!!! your answer is correct.")
       print("Number of entries: ", count)
       print()
       break
       print()
    P5HW2_menu.menu()
    add = True
    while add ==True:
        print()
        add = input("Please choose one of the menu options: ")
        print()
        if add =="1":
            quiz_add()
        elif add =="2":
            quiz_sub()
        elif add =="3":
            print("Thank you for playing...")
            print("bye!!!")
            exit()

def quiz_sub():
    random_n = random.randint(0,100)
    rand_n = random.randint(0,100)
    answer2 = random_n - rand_n
    count = 0
    while ans !=2:
     count = count + 1
     print(" ", random_n)
     print("-", rand_n)
     print("Enter answer.")
     user_ans = int(input())
     if user_ans > answer2:
       print("Sorry, guess is too high.")
       print("Try again.")
     elif user_ans < answer2:
       print("Sorry, guess is too low.")
       print("Try again.")
       print()
     else:
       user_ans == answer2
       print("Congratulations!!! your answer is correct.")
       print("Number of entries: ", count)
       print()
       break
       print()
    P5HW2_menu.menu()
    sub = True
    while sub == True:
        print()
        sub = input("Please choose one of the menu options: ")
        print()
        if sub=="1":
             quiz_add()
        elif sub =="2":
            quiz_sub()
        else:
            sub=="3"
            print("Thank you for playing...")
            print("bye!!!")
            exit()

#---------------------------------------------------------------------#            


import P5HW2_menu
ans = True
while ans == True:
    print()
    ans=input("Please choose one of the menu options: ")
    print()
    if ans=="1":
        print("")
        quiz_add()
    elif ans=="2":
        print("")
        quiz_sub()
    else:
        ans=="3"
        print("Thank you for playing...")
        print("bye!!!")
        exit()

#--------------------------------------------------------------------#


# START
# Program is a random generated math quiz game.
# P5HW2_menu is the main menu on a separate file and imported into the main file.
# Import section for main menu is at the bottom of the main code in order to-
# -refer to functions by the user's choice.
# PRINT Welcome to Math Quiz
# IMPORT P5HW2_menu
# ans--> True
# WHILE ans --> True
# ans--> User will input a number based off of main menu choices.
# PRINT Please choose one of the menu choices:
# IF the user enters 1,
# THEN call quiz_add() function
# ELIF user enters 2,
# THEN call quiz_sub() function
# ELSE the user enters 3,
# Program will terminate and display the following message:
# PRINT Thank you for playing...
# PRINT Bye!!!
# exit()
# ENDIF
#
# quiz_add()--> takes two random numbers and adds them together.
# IF the user enters the solution incorrectly,
# THEN the program will display the follwing message:
# PRINT Too low. Try again. OR Too High. Try again.
# User is prompted to enter the correct solution.
# ENDIF
# IF the user enters the solution correctly,
# THEN PRINT Congratulations!!! Your answer is correct.
# PRINT Number of entries:, count
# count--> Num of entries
# P5HW2_menu.menu() is then called in order to display-
# - the main menu chart after a problem is solved.
#
# quiz_sub()--> takes two random numbers and subtracts them. 
# IF the user enters the solution incorrectly,
# THEN the program will display the follwing message:
# PRINT Too low. Try again. OR Too High. Try again.
# User is prompted to enter the correct solution.
# ENDIF
# IF the user enters the solution correctly,
# THEN PRINT Congratulations!!! Your answer is correct.
# PRINT Number of entries:, count
# P5HW2_menu.menu() is then called in order to display-
# - the main menu chart after a problem is solved.
#
# Options are provided at the end of each functions loops-
# - in order to continue looping the menu after problems are solved-
# - until the 3 option is entered.
#END



