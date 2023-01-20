a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a > b:
    a = b
else:
    a = a
if c > d:
    c = d
else:
    c = c
if a < c:
    print(a)
else:
    print(c)
