a, b, c = int(input()), int(input()), int(input())
if (c - b) == (b - a) and a <= b <= c or a > b > c:
    print('YES')
else:
    print('NO')
