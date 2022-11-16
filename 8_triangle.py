a, b, c = int(input()), int(input()), int(input())
triangle = 'YES' if b+c>a and c+a>b and b+a>c else "NO"
print(triangle)
