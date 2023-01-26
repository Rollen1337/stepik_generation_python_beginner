n = int(input())
l = n % 10
flag = True

while n != 0:
    t = n % 10
    if l > t:
        flag = False
    else:
        l = t
    n //= 10
if flag is True:
    print('YES')
else:
    print('NO')