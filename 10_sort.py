a, b, c = int(input()), int(input()), int(input())
if a >= b >= c and a >= c:
    print(c, b, a)
elif b >= a >= c and b >= c:
    print(c, a, b)
elif a <= b <= c and a <= c:
    print(a, b, c)
elif a >= b and a >= c >= b:
    print(b, c, a)
elif b <= a <= c and b <= c:
    print(b, a, c)
else:
    print(a, c, b)
