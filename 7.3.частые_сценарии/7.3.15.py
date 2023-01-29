nf = int(input())               
n1 = 0                       
n2 = 1                       
for _  in range(nf):             
    n2 = n1 + n2          
    n1 = n2 - n1         
    print(n1, end=' ')