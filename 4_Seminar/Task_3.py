# 3 Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# sequence_list = list[1, 2, 2, 4, 8, 8, 23, 32, 5, 1, 5, 4].split()
# sequence_intlist = list(map(int, sequence_list))
# for i in sequence_list:
#     print(sequence_list[i])

entered_list = [int(i) for i in input('Введите элементы списка через пробел: ').split()]
sequence_list = []
for i in entered_list:
   if entered_list.count(i) == 1:
    sequence_list.append(i)
print(sequence_list)