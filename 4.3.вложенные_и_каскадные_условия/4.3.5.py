a, b, c = int(input()), int(input()), int(input())
if a < b < c or a > b > c:
    print(b)
elif b < c < a or b > c > a:
    print(c)
else:
    print(a)