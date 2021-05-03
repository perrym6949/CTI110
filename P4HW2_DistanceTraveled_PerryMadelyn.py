#CTI-110
#P4HW2 - Distance Traveled
#Madelyn Perry
#4/14/2021
#


car_sp = float(input("Enter car's speed: "))
time_t = int(input("Enter time traveled: "))
dist = 0
print()


if time_t <= 0:
    print("Error! time entered should be >0")
    print()
    time_t = int(input("Please Enter time traveled: "))
    print()
    print("Time\tDistance")
    print("-----------------")
    for i in range(1, time_t + 1):
        print(format(i, '1.0f'), '\t', format(i * car_sp, '6.1f'))
        dist += i * car_sp
else:
    time_t <= 1
    print()
    print("Time\tDistance")
    print("-----------------")
    for i in range(1, time_t + 1):
        print(format(i, '1.0f'), '\t', format(i * car_sp, '6.1f'))
        dist += i * car_sp


print()
print()

def_time = input("Do you want to enter a different time? (y/n): ")

while def_time == "y":
    time_t = int(input("Please Enter time traveled: "))
    print()
    print("Time\tDistance")
    print("-----------------")
    for i in range(1, time_t + 1):
        print(format(i, '1.0f'), '\t', format(i * car_sp, '6.1f'))
        dist += i * car_sp
    def_time = input("Do you want to enter a different time? (y/n): ")


   
# START
# Program is to calulate time and speed that the user enters and get distance traveled.
# PRINT Enter car's speed:
# The user enters the car's speed.
# PRINT Enter time traveled:
# The user enters the time.
# IF the user enters time <=0
# THEN PRINT Error! Time entered should be >0
# ENDIF
# PRINT Please Enter car's speed:
# The user enters a valid number.
# PRINT Time \t Distance
# PRINT "----"
# CALCULATE Time and Distance --> dist += i * car_sp
# LOOP -->  for i in range(1, time_t + 1)
# Time starts at 1 and increases based on how much the user enters for time.
# PRINT number of hours with distance for each hour.
# PRINT Do you want to enter a different time? (y/n):
# WHILE the user enters y, then the user will be prompted to enter another time
# PRINT Time and Distance calculations below line
# IF the user --> n, while loop will discontinue.
# ENDIF
# END
