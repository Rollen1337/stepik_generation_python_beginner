n = int(input())         
ma = 0                 
mi = 9                 
while n != 0:            
    if n % 10 > ma:    
        ma = n % 10    
    if n % 10 < mi:    
        mi = n % 10    
    n = n // 10          
print(f"Максимальная цифра равна {ma}")
print(f"Минимальная цифра равна {mi}") 