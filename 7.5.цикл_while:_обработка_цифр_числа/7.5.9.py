n = int(input())       
flag = True              
while n > 9:           
    l = n % 10      
    n = n // 10         
    s = n % 10           
    if l != s:      
        flag = False         
if flag:                 
    print('YES')         
else:                
    print('NO') 