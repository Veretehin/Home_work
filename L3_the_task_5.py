num = 0
try:
    while True:
        for i in map(int, input('Введите числа через пробел. Для выхода введите любуой текст или букву: ').split()):
            num += i
        print(num)
except ValueError:
    print(num)