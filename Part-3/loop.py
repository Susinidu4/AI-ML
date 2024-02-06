x = ["apple" , "banana" , "berry" , 45 , 56.7 , True]

#while
i = 0 
while i < len(x):
    print(x[i])
    i = i + 1

print()

#for
#range(0,6) -> 0,1,2,3,4,5
for i in range(0, len(x)):
    print(x[i])

print()

#for each
for item in x:
    print(item)
