# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_func(s, e):
    try:
        x = s / e
        return x
    except ZeroDivisionError:
        return "Деление на ноль запрещено!"
    except ValueError:
        print('Вы ввели не число!')
print('Результат деления = ', my_func(int(input("Введите делимое: ")), int(input("Введите делитель: "))))
