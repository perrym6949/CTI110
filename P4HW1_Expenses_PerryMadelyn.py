#CTI-110
#P4HW1 - Expenses
#Madelyn Perry
#4/13/2021
#

start_amt = float(input("Enter starting amount in account: $"))
print()
moreExpense = "y"

totalExpenses = 0

count = 0

while moreExpense.lower() == "y":
    expense = float(input("Enter expense: "))
    count = count + 1
    totalExpenses = totalExpenses + expense
    moreExpense = input("Do you want to enter another expense? (y/n): ")
    print()
    total = start_amt - totalExpenses
    if moreExpense == "n":
        total = start_amt - totalExpenses
        print("Amount in account before expenses subtracted: $",start_amt)
        print("Number of expenses entered", count)
        print("Amount in account after expenses is subtracted is: $",total)




# START
# Program is to calculate number of expenses withdrawn from users account.
# Program enters as many entries the user allows.
# PRINT Enter starting amount in account $
# User enters value.
# moreExpense --> "y"
# PRINT Enter expense
# User enters the first expense.
# PRINT Do you want to enter another expense? (y/n):
# IF user enters "y"
# THEN while loop will continue the steps and subtract the numbers entered.
# IF user enters "n"
# THEN results will display at the bottom of the screen.
# ENDIF
# PRINT Amount in account before expenses subtracted $, start_amt
# PRINT Number of expenses entered, count
# PRINT Amount in account after expenses is subtracted is $, total
# END
#
