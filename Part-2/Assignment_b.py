#Create a python program to input marks of 10 students and print the maximum mark, minimum mark and average mark of the students.

marks = int(input("Enter mark : "))
min = marks
max = 0
x = 1
sum = 0

while x <= 10:

    if marks > max:
        max = marks

    if marks < min:
        min = marks

    sum = sum + marks

    x += 1
    
    if x <= 10:    
        marks = int(input("Enter mark : "))

print("Maximum marks = ", max)
print("Minimum marks = ", min)
print("Average marks = ", sum/10)