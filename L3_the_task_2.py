#Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
#имя, фамилия, год рождения, город проживания, email, телефон.
#Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


def my_func(**kwargs):
    return ' '.join(kwargs.values())

    print(my_func(name = input('enter name'),surname = input('enter surname'), year = input('enter year'), city = input('enter city'), email = input('enter email'), phone = input('input telephone')))

