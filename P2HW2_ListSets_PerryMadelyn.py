#CTI-110-0902
#P2HW2 - List and Sets
#Madelyn Perry
#3/9/2021
#

#creates empty list
listA = []

#asking how many numbers to input in list
num = int(input("Please Enter the length of the list: "))

#append numbers in list
for i in range(1, num + 1):
	num= int(input("Enter Numbers: "))
	listA.append(num)

print("List set:", set(listA)) #converts list into set and display

print("The Lowest Number:", min(listA))
print("The Highest Number:", max(listA))
total = sum(listA)
print("Total of Numbers:", total)
length = len(listA)
average = total / length
print("Average of Numbers:", average)



# START
# Empty list is created
# IF user enters len --> 10
# THEN 10 numbers are to be inputted by the user
# IF user enters --> 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 manually
# THEN list will display as [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# END IF
# CONVERT inputted list into SET
# PRINT SET
# IF duplicates are entered, duplicates will not show up in SET --> True
# ENDIF
# DISPLAY the lowest number in list
# IF lowest number --> 0
# THEN lowest number --> 0 is TRUE
# ENDIF
# DISPLAY highest number inputted
# DISPLAY total of listed numbers added together
# LEN is = to how many numbers are in the list
# AVERAGE is total divided by length
# DISPLAY the average of the listed numbers
# END
#



