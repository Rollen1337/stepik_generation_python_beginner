n = int(input())
for i in range(1, n + 1):
    if i in range(5, 10) or i in range(17, 38) or i in range(78, 88):
        continue      
    print(i)