n = int(input())
a = n % 10
b = (n % 100) // 10
c = n // 100
summ = a + b + c
umn = a * b * c
print(f"Сумма цифр = {summ}")
print(f"Произведение цифр = {umn}")