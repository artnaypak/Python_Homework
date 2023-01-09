# 2 Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

user_strlist = input('Enter several numbers divided by a "space" key: ').split() # Метод split() делит введенную строку на список подстрок.
print(user_strlist) 

user_intlist = list(map(int, user_strlist)) # map() переводит в int() каждый элемент ранее введенного списка.
print(user_intlist)

i = 0
while i < len(user_intlist) / 2:
    print(user_intlist[i] * user_intlist[len(user_intlist) - i - 1])
    i += 1

