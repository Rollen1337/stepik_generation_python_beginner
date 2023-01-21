a = input()
b = input()
if a == 'красный' and b == 'синий' or a == 'синий' and b == 'красный':
    print('фиолетовый')
elif a == 'красный' and b == 'красный':
    print('красный')
elif a =='красный' and b =='желтый' or a =='желтый' and b =='красный':
    print('оранжевый')
elif a =='желтый' and b =='желтый':
    print('желтый')
elif a =='синий' and b =='желтый'or a =='желтый' and b =='синий':
    print('зеленый')
elif a =='синий' and b =='синий':
    print('синий')
else:
    print('ошибка цвета')