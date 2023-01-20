n = int(input())
pp = n // 1000 + n % 10
vt = (n % 10 ** 3) // 10 ** 2 - (n % 100) // 10
if pp == vt:
    print('ДА')
else:
    print('НЕТ')
