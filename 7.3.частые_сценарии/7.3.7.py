from math import *
n = int(input())
count = 0
for i in range(1, n + 1):
    count += (1 / i)
print(count - log(n))