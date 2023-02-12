n = int(input())
kentron = n // 2 + 1         
cunt = 0                   
for i in range(1, n + 1):
    if i > kentron:           
        cunt -= 1          
    else:
        cunt += 1          
    
    for _ in range(cunt):  
        print('*', end='')
    print()