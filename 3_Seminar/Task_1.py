# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

list1 = [1, 9, 11, 23, 4, 3]
uneven_number_index = 1
uneven_sum = 0

for i in list1:
    if i < len(list1):
        uneven_number = list1[uneven_number_index]
        print(uneven_number)
        uneven_number_index += 2
        uneven_sum += uneven_number
print()
print(f'the sum of the digits with uneven position is {uneven_sum}')


        