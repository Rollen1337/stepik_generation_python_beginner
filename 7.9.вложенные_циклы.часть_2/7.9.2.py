n = int(input())

for i in range(1, n + 1):   
    cunt = 0                 
    for j in range(i):        
        cunt += 1            
        print(cunt, end='')  
    for k in range(i, 1, -1): 
        cunt -= 1            
        print(cunt, end='')  
    print()