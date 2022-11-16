a, b, c = int(input()), int(input()), int(input())
equals = 0
if a == b and b == c:
    equals = 3
else:
    if a == b or b == c or c == a:
        equals = 2
print(equals)
