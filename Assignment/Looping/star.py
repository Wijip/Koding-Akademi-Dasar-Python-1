row = 5
for i in range(0, row):
    for j in range(0,i + 1):
        print("* ",end='')
    print(" ")

print("")

for i in range(row + 1, 0, -1):
    for j in range(0, i -1):
        print("* ",end='')
    print(" ")

print("")
for i in range(row):
    for j in range(row):
        print("* ",end="")
    print("")