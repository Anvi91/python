# Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

sec_inp = int(input('Введите количество секунд '))
print(f'{sec_inp // 3600}:{sec_inp % 3600 // 60}:{sec_inp % 3600 % 60}')
