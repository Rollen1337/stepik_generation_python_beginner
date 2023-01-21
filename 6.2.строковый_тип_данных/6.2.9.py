a, b, c = len(input()), len(input()), len(input())
summa = a + b + c
abcmin = min(a, b, c)
abcmax = max(a, b, c)
if summa == (abcmin + abcmax) / 2 * 3:
    print("YES")
else:
    print("NO")