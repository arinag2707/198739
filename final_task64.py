# Задача 64: Задайте значение N. Напишите программу, которая выведет все натуральные числа в промежутке от N до 1. 
# Выполнить с помощью рекурсии.

def print_numbers_recursive(n):
    if n <= 0:
        return
    print(n, end=', ' if n > 1 else '\n')
    print_numbers_recursive(n - 1)

N = 5
print_numbers_recursive(N)

N = 8
print_numbers_recursive(N)
