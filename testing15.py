# matrix1 = [
#     [9, 7],
#     [2, 8],
# ]
# matrix2 = [
#     [4, 1],
#     [1, 5],
# ]
#
# for x in range(0, len(matrix1)):
#     for y in range(0, len(matrix2[0])):
#         print(matrix1[x][y] - matrix2[x][y], end='')
#     print(' ')

# n=5
# i = 0
# while(i<=n):
#     print(" " * (n - i) + "* " * i)
#     i += 1
# print()
# row = 5
# for i in range(row + 1, 0, -1):
#     for j in range(0, i - 1):
#         print("* ", end="")
#     print("")
# print("")

# size = 5
# m = (2 * size) - 2
# for i in range(0, size):
#     for j in range(0, m):
#         print(end=" ")
#     # decrementing m after each loop
#     m = m - 1
#     for j in range(0, i + 1):
#         print("* ", end=' ')
#     print(" ")
#
# print()

rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")

print("\nCh")
rows = 5
i = rows - 1
while i >= 0:
    j = 0
    while j < i:
        print('', end=' ')
        j += 1
    k = i
    while k <= rows - 1:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1

print("\nsegitiga")
rows = 5
i = 0
while i <= rows - 1:
    j = 0
    while j < i:
        # display space
        print('', end=' ')
        j += 1
    k = i
    while k <= rows - 1:
        print('*', end=' ')
        k += 1
    print()
    i += 1

i = rows - 1
while i >= 0:
    j = 0
    while j < i:
        print('', end=' ')
        j += 1
    k = i
    while k <= rows - 1:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1