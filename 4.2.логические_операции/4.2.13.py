g = int(input())
if (g % 4 == 0 and g % 100 != 0) or g % 400 == 0:
    print('YES')
else:
    print('NO')