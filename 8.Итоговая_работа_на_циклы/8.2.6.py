num = int(input())
count_digit_3 = 0
count_last_digit = 0
last_digit_for_count = num % 10
count_even_digit = 0
total_digit_higher_5 = 0
total_digit_higher_7 = 1
count_digit_0_5 = 0

while num != 0:
    last_digit = num % 10
    if last_digit == 3:
        count_digit_3 += 1
    if last_digit == last_digit_for_count:
        count_last_digit += 1
    if last_digit % 2 == 0:
        count_even_digit += 1
    if last_digit > 5:
        total_digit_higher_5 += last_digit
    if last_digit > 7:
        total_digit_higher_7 *= last_digit
    if last_digit == 0 or last_digit == 5:
        count_digit_0_5 += 1
    num //= 10
print(count_digit_3)
print(count_last_digit)
print(count_even_digit)
print(total_digit_higher_5)
print(total_digit_higher_7)
print(count_digit_0_5)