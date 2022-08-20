# 7)Создать вручную и заполнить несколькими строками текстовый файл, в котором
# каждая строка должна содержать данные о фирме: название, форма собственности,
# выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а
# также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли
# ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их
# прибылями, а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить ее в словарь (со значением убытков).
# Пример списка:
# [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.


import json

dict_profit = {}
dict_lesion = {}
dict_aver = {}
average_profit = 0
final_list = []
with open('task7', 'r', encoding='utf-8') as my_file:
    for line in my_file:
        name_firm, firm, profit, costs = line.split()
        if int(profit) > int(costs):
            dict_profit[name_firm] = int(profit) - int(costs)
            average_profit = average_profit + int(profit) - int(costs)
        elif int(profit) < int(costs):
            dict_lesion[name_firm] = int(profit) - int(costs)
    dict_aver['average_profit'] = average_profit
final_list.append(dict_profit)
final_list.append(dict_aver)
final_list.append(dict_lesion)
print(final_list)
with open('exit_file.json', 'w') as my_file2:
    json.dump(final_list, my_file2)
