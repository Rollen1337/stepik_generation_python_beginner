a = int(input())
b = a % 10
c = a % 100 // 10
if b == 0 and c == 0:
    print('YES')
else:
    print('NO')