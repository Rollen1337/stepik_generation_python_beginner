n = int(input())
cunt = 0
for i in range(1, n + 1):
    k = i ** 2
    if k % 10 == 2 or k % 10 == 5 or k % 10 == 8:
        cunt += i
print(cunt)
