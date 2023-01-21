a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if b1 < a2 or b2 < a1:
    print('пустое множество')
else:
    if a1 > a2:
        a2 = a1
    if b1 > b2:
        b1 = b2
    if a2 == b1:
        print(a2)
    else:
        print(a2, b1)