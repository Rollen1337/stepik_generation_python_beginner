n = int(input())             
cunt = 0                      
for y in range(1, n + 1):    
    for x in range(y):         
        cunt += 1             
        print(cunt, end=' ')  
    print() 