n = int(input())           
summ = 0                   
f = 1                

for i in range(1, n + 1):   
    for j in range(1, i + 1):  
        f *= j      
    summ += f       
    f = 1            
print(summ)