n = int(input())      

while n > 9:          
    s = 0    
    while n > 0:
        ll = n % 10  
        s += ll   
        n = n // 10          
    n = s
    
print(n)