from math import sqrt
a, b, c = float(input()), float(input()), float(input())
d = b**2 - 4*a*c
if d > 0:
    x1 = (-b + sqrt(d))/(2*a)
    x2 = (-b - sqrt(d))/(2*a)
    print(x1)
    print(x2)
elif d == 0:
    x1 = (-b) / (2 * a)
    print(x1)
