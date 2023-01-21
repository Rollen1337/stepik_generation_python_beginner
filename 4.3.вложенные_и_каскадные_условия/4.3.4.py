a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print('Равносторонний')
elif a == b or a == c or b == c:
    print('Равнобедренный')
else:
    print('Разносторонний')
