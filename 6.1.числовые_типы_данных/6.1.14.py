n = int(input())
a = n % 10
b = (n % 100) // 10
c = n // 100
maxim = max(a, b, c)
minxim = min(a, b, c)
avgxim = (a + b + c) - maxim - minxim
if maxim - minxim == avgxim:
    print(f"Число интересное")
else:
    print(f"Число неинтересное")