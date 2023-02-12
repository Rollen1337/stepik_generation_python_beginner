n = int(input())
while n >= 100:
    s = n % 10
    n //= 10
print(s)