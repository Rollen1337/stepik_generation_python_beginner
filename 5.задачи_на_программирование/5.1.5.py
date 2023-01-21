n = int(input())
if n % 2 != 0:
    print("YES")
if n % 2 == 0 and n >= 2 and n <= 5:
    print("NO")
if n % 2 == 0 and n >= 6 and n <= 20:
    print("YES")
if n % 2 == 0 and n > 20:
    print("NO")