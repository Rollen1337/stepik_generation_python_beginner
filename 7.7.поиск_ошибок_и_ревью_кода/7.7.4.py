mx = 0
s = 0
for i in range(10):
    x = int(input())
    if x < 0:
        s += x
        if mx == 0 or x > mx:
            mx = x
if s:            
    print(s)
    print(mx)
else:
    print('NO')