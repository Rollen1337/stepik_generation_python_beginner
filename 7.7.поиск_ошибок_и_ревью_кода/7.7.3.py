count = 0
p = 1  
for i in range(1, 11):  
    x = int(input())
    if x > -1:  
        p *= x
        count += 1
if count > 0:
    print(count)  
    print(p)
else:
    print('NO')