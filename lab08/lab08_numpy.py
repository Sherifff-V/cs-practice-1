import numpy as np

# 1

# hours — числа 0-21 с шагом 3
hours = np.arange(0, 22, 3)
print("hours:", hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)

line = np.linspace(0, 1, 5)
print("line:\n", line)

zeros = np.zeros(6, dtype=int)
print("zeros:\n", zeros)


x_table = np.array([[-1, -1, -1],
                    [-1, -1, -1]])
print("unknown_table:\n", x_table)

identity = np.eye(3)
print("identity:\n", identity)

# 2

print("2 задание \nТретий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2–5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("Массив в обратном порядке:", hours[::-1])


# 3

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("Форма:", temperatures.shape)
print("Число измерений:", temperatures.ndim)
print("Число элементов:", temperatures.size)

print("Значение из второй строки и третьего столбца:", temperatures[1, 2])
print("Первая строка:", temperatures[0])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:\n", temperatures[:2, 1:])
print("Центральный фрагмент 2×2:\n", temperatures[0:2, 1:3])

# 4

matrix = np.arange(1, 26).reshape(5, 5)
print("Исходная matrix:\n", matrix)

first_three = matrix[:3]
print("Первые три строки:", first_three)
print(first_three.shape)

last_two = matrix[-2:]
print("Последние две строки:\n", last_two)
print(last_two.shape)

first_two_cols = matrix[:, :2]
print("Первые два столбца:", first_two_cols)
print( first_two_cols.shape)

fragment = matrix[1:4, 2:5]
print("Фрагмент:", fragment)
print(fragment.shape)

corner = matrix[-2:, -2:]
print(corner)
print(corner.shape)

# 5

changed_hours = hours.copy()
changed_hours[2:5] = 99         
changed_hours[::2] = -1          

print("\nchanged_hours:", changed_hours)
print("исходный hours:", hours)


small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9
print("small_matrix после изменения:\n", small_matrix)
# Комментарий: .copy() нужна, чтобы changed_hours был независимой копией.
# Если написать changed_hours = hours, то обе переменные ссылались бы на один
# и тот же массив, и изменения в changed_hours изменили бы исходный массив.

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0         
changed_matrix[:, -1] = -1       
changed_matrix[1:4, 1:4] = 100   

print("\nисходная матрица:\n", matrix)
print("\nизмененная матрица:\n", changed_matrix)

# 6

numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print("numbers:", numbers)
print("shape numbers:", numbers.shape)
print("\ntable:\n", table)
print("shape table:", table.shape)
print("\ntransposed:\n", transposed)
print("shape transposed:", transposed.shape)

# reshape(3, 4) работает, потому что 3 * 4 = 12,
# а в numbers ровно 12 элементов. Вызов, наприммер reshape(5, 3) привёл бы к ошибке,
# так как 5 * 3 = 15