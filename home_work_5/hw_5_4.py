# 3. Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов (не менее 10 строк). Определить, кто из
# сотрудников имеет оклад менее 20 тыс.,вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open('task4', 'r', encoding='utf-8') as my_file:
    my_lines = my_file.readlines()
    print(f'Оклад меньше 20000 у сотрудников:')
    sale = []
    for el in my_lines:
        i = el.split()
        sale.append(float(i[1]))
        if float(i[1]) < 20000:
            print(f'{i[0]}')

    print(f'Средний доход: {round(sum(sale) / len(sale), 2)}')