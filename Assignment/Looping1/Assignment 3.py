n = 5
for i in range(0,n):
    for j in range(0,i+1):
        print("* ", end='')
    print('')

print()

for i in range(1, n +1):
    for j in range(1, n+1):
        if j <=i:
            print("* ",end=" ")
        else:
            print("* ",end=" ")
    print()