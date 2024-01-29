#Write a program to input a series of numbers terminated by -999. Calculate and print the sum of the numbers entered. 

no = int(input("Enter series of numbers (Enter -999 to stop the process) : "))
sum = 0
while no != -999:

    sum = sum + no 
    no = int(input("Enter series of numbers (Enter -999 to stop the process) : "))

print("Sum of the numbers : ", sum)