# 3 Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# new_lst = [round(i % 1, 2) for i in lst if i % 1 != 0]
# print(max(new_lst) - min(new_lst))

user_floatlist = list(map(float, input('Enter several real numbers (as 1.01) divided by a "space" key: ').split())) # введенные "строковые" значения сразу преобразуются в float
print(user_floatlist) 

new_list = [round(i % 1, 2) for i in user_floatlist if i % 1 != 0]
print(max(new_list) - min(new_list))