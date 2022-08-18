# 2)Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('task2.txt', 'r', encoding='utf-8') as my_file:
    my_lines = my_file.readlines()
    print(f'Мой файл: {my_lines}')
    print(f'Количество строк: {len(my_lines)}')
    for el in my_lines:
        print(f'Количество слов в строке: {len(el.split())}')
