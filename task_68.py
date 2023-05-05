# Задача 68: Напишите программу вычисления функции Аккермана с помощью рекурсии. Даны два неотрицательных числа m и n.
# m = 2, n = 3 -> A(m,n) = 9
# m = 3, n = 2 -> A(m,n) = 29

def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))

m1, n1 = 2, 3
result1 = ackermann(m1, n1)
print(f"A({m1}, {n1}) = {result1}")

m2, n2 = 3, 2
result2 = ackermann(m2, n2)
print(f"A({m2}, {n2}) = {result2}")