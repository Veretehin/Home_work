#Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
all_seconds = int(input("Введите время в секундах : "))
hours = all_seconds // 3600
minutes = (all_seconds - hours * 3600) // 60
seconds = all_seconds - (hours * 3600 + minutes * 60)
print(f'Время : {hours} : {minutes} : {seconds}')