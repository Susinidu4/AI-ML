#1st method
birth = int(input("Enter year of birth : "))

if birth <= 2006:
    print("You are an adult..")
else:
    print("You are a child")

print(" ")

#2nd method
birth = int(input("Enter year of birth : "))

age = 2024 - birth

if age >= 18:
    print("You are an adult..")
else:
    print("You are a child")