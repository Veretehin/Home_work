# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
a = seasons_list
b = seasons_dict
month = int(input("Введите месяц по номеру: "))
if 3 >= month or month == 12:
    print(a[0])
    print(b[1])

elif 3 < month <= 6:
    print(a[1])
    print(b[2])

elif 6 < month >= 8:
    print(a[2])
    print(b[3])

elif 8 < month >= 11:
    print(a[3])
    print(b[4])

else:
    print("Такого месяца не существует!")
