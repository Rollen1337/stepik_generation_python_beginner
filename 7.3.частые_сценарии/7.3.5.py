a = int(input())
b = int(input())
counter = 0
for i in range(a, b + 1):
    if i % 10 == 4 or i % 10 == 9:
        counter += 1
print(counter)
