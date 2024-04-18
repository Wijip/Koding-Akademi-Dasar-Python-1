import math

a = int(input("Masukkan angka 1 : "))
b = int(input("Masukkan angka 2 : "))
c = int(input("Masukkan angka 3 : "))
d = (b**2) - (4*a*c)

x1 = (-b + math.sqrt(d)) / (2 * a)
x2 = (-b - math.sqrt(d)) / (2 * a)

print('Solusinya adalah {0} dan {1}'.format(x1, x2))
