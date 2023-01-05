# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:

# - 6782 -> 23
# - 0,56 -> 11

n = int(input("Enter the number: "))
sum = 0
 
while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10
 
print("Sum of digits of the given number is:", sum)
