a = int(input())
b = int(input())
max1 = 0
max2 = 0
for i in range(a, b + 1):
    max1 = 0
    for j in range(1, i + 1):
        if i % j == 0:
            max1 += j
    if max1 >= max2:
        max2 = max1
        x = i
        max1 = 0
print(x, max2)