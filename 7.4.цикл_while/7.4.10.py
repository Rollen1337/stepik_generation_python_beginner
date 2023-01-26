n, b = input(), 0
while n not in ('стоп', 'хватит', 'достаточно'):  
    b += 1 
    n = input()        
print(b)