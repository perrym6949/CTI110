# System Grading Output
# 3/23/2021
# CTI-110 P3HW1-Debugging
# Madelyn Perry
#


def main():
    # Program takes number grade and outputs letter grade.

    # Use 10-point grading scale:
 A = 90
 B = 80
 C = 70
 D = 60
 F = 50
    
score = input('Please input your grade: ') 
Grd = int(score) # Grd <-- Grade
if Grd>=90:
    print('Your grade is: A.')
elif Grd>=80:
    print('Your grade is: B.')
elif Grd>=70:
    print('Your grade is: C.')
elif Grd>=60:
    print('Your grade is: D.')
else:
    print('Your grade is: F.')
    
 








main()
