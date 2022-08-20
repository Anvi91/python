# 4)	Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую
# построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


translation = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('task3_1', 'r', encoding='utf-8') as my_file:
    my_lines = my_file.readlines()
    for el in my_lines:
        i = el.split(' ', 1)
        new_file.append(translation[i[0]] + ' ' + i[1])

with open('task3_2', 'w', encoding='utf-8') as my_file2:
    my_file2.writelines(new_file)
