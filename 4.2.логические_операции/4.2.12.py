a, b, c = int(input()), int(input()), int(input())
if b < a + c and a < b + c and c < a + b:
    print("YES")
else:
    print("NO")