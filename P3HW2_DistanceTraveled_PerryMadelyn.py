# CTI-110
# P3HW2 - Distance Traveled
# Madelyn Perry
# 3/25/2021
#




car_sp = float(input("Please Enter car's speed:"))
time_t = float(input("Please Enter time traveled:"))


if time_t <= 0:
    print("Error! time entered should be >0")
    time_t = (0 + 1)
    print("Speed entered:", car_sp)
    print("Time entered:", time_t)
    time_d = car_sp * time_t
    print("Distance traveled:", time_d, "miles")
    
else:
    time_t<= 1
    print("Speed entered:", car_sp)
    print("Time entered:", time_t)
    time_d = car_sp * time_t
    print("Distance traveled:", time_d, "miles")

    
# START
# PRINT "Please Enter car's speed:"
# car_sp input is float
# user types in car speed
# PRINT"Please Enter time traveled:"
# time_t input is float
# This program is made to detect errors in users input
# IF user inputs 0 or negative number
# THEN PRINT "Error! time entered should be >0"
# ENDIF
# Correct this error with time_t <-- 0 + 1
# PRINT "Speed entered:" <-- car_sp
# PRINT "Time entered:" <-- time_t
# time_d <-- car_sp * time_t
# This takes car speed and time traveled multiplied and equal to distance.
# PRINT "Distance traveled:", time_d, "miles"
# IF user enters a number greater than 1,
# THEN number is TRUE
# ENDIF
# PRINT "Speed entered:" <-- car_sp
# PRINT "Time entered:" <-- time_t
# time_d <-- car_sp * time_t
# PRINT "Distance traveled:", time_d, "miles"
# END
#



    
    

    
