a, b, c = int(input()), int(input()), int(input())
type_of_triangle = ''
if b+c > a and c+a > b and b+a > c:
    if a**2 + b**2 < c**2 or a**2 + c**2 < b**2 or c**2 + b**2 < a**2:
        type_of_triangle = 'obtuse'
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2:
        type_of_triangle = 'right'
    else:
        type_of_triangle = 'acute'
else:
    type_of_triangle = 'impossible'
print(type_of_triangle)
