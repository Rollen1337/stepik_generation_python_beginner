x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
x = x2 - x1  
y = y2 - y1  
if -1 <= x <= 1 and -1 <= y <= 1:
    print('YES')
else:
    print('NO')