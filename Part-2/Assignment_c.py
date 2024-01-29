#Create a program to input five marks of a student and display the grades. 

#• Mark > 75 – A 
#• Mark 65 to 75 – B 
#• Mark 55 to 64 – C 
#• Mark 45 to 54 – S 
#• Mark < 45 – F 

x = 1
while x < 5:
    mark = int(input("Enter mark : "))
    if mark >= 75:
        print("Grade A")
    elif mark >= 65 and mark < 75:
        print("Grade B")
    elif mark >= 55 and mark < 64:
        print("Grade C")
    elif mark >= 45 and mark < 54:
        print("Grade S")
    elif mark < 45:
        print("Grade F")

    x += 1
