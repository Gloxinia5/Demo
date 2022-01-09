height = int(input("Enter the height"))

#half pyramid
for i in range(height + 1):
    for j in range(i):
        print("#", end = "")
    print(" ")


#reverse half pyramid
for i in range(height + 1):
    for j in range(height - i):
        print(" ", end = "")
    for h in range(i):
        print("#",end = "")
    print(" ")

#pyramid
for i in range(height + 1):
    for j in range(height - i):
        print(" ", end = "")
    for h in range(i + i):
        print("#",end = "")
    print(" ")
print(" ")

#180 degree half pyramid
for i in range(height + 1):
    for j in range(height - i):
        print("#", end = "")
    print(" ")

for i in range(height + 1):

    for j in range(height - i):
        print("#", end = "")
    print("")
    for h in range(i + 1):
        print(" ", end = "")
print("")

#180 degree pyramid
for i in range(height + 1):
    for j in range(i+1):
        print(" ", end = "")
    for h in range(((height + height) - j) - j):
        print("#", end = "")
    print()

