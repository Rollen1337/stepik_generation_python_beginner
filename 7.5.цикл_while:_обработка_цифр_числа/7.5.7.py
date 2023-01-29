n = int(input())   
nput = n                       
a = 0                        
b = 1                       
c = 0                         
while nput != 0:                
    a += nput % 10          
    b *= nput % 10       
    c += 1                    
    nput //= 10                  
print(a)                      
print(c)                      
print(b)                    
print(a / c)                
print(n // 10 ** (c - 1))         
print(n // 10 ** (c - 1) + n % 10)  