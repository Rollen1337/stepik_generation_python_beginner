n = int(input())
cunter = 0
for _ in range(1, n + 1):
    if n % _ == 0:
        cunter += _
print(cunter)        