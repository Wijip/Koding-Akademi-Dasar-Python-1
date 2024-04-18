n = 5
for i in range(1, n+1):
    for j in range(1, n+1):
        print("* ",end=' ')
    print("")


print()

rows = 5
b = 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print("* ", end=' ')
    print('\r')

print()

for i in range(rows, 0, -1):
    num = i
    for j in range(0, i):
        print("* ", end=' ')
    print("\r")

print()
# rows = 6
# for row in range(1, rows):
#     for column in range(row, 0, -1):
#         print(column, end=' ')
#     print("")
rows = 5
for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    print()