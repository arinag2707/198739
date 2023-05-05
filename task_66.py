# Задача 66: Задайте значения M и N. Напишите программу, которая найдёт сумму натуральных элементов в промежутке от M до N.
# M = 1; N = 15 -> 120
# M = 4; N = 8. -> 30

def sum_of_natural_numbers(m, n):
    return sum(range(m, n + 1))

M1, N1 = 1, 15
result1 = sum_of_natural_numbers(M1, N1)
print(f"Сумма натуральных чисел от {M1} до {N1}: {result1}")

M2, N2 = 4, 8
result2 = sum_of_natural_numbers(M2, N2)
print(f"Сумма натуральных чисел от {M2} до {N2}: {result2}")