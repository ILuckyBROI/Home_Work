# Выяснить тип результата выражений:
# 15 * 3
# 15 / 3
# 15 // 2
# 15 ** 2
print('Проверка: ', type(15 * 3), end=" ")
print(type(15 / 3), end=" ")
print(type(15 // 2), end=" ")
print(type(15 ** 2))

operation = [15 * 3, 15 / 3, 15 // 2, 15 ** 2]
print('Результат: ', end=" ")
for i, exp in enumerate(operation):
    print(type(exp), end=" ")
