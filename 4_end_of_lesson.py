n = int(input())
end_of_lesson = (n//2)*5 + n*45 + ((n+1)//2-1)*15
print(9 + end_of_lesson//60, end_of_lesson % 60)
