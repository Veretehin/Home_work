#Создать текстовый файл (не программно), сохранить
#в нем несколько строк, выполнить подсчет количества строк,
#количества слов в каждой строке.

my_list = ['Hello\n', 'Chao\n', 'Hola\n']
with open("test_2.txt", 'w+') as file_obj:
    file_obj.writelines(my_list)
with open("test_2.txt") as file_obj:
    lines = 0
    words = 0
    for line in file_obj:
        lines += 1 #line.count("\n")
        words = len(line.split())
        print(f"{words} cлов в строке")
print(f"количество строк {lines}")
