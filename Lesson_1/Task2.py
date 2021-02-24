# Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
# Вычислить сумму тех чисел из этого списка, сумма цифр которых
# делится нацело на 7. Например, число «19 ^ 3 = 6859» будем
# включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело
# на 7. Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму
# тех чисел из этого списка, сумма цифр которых делится нацело
# на 7. Внимание: новый список не создавать!!!
cubNumbers = []
numbers = []
sumDiv7 = 0
for i in range(1, 1001, 2):
    cubNumbers.append(i ** 3)
for ind, val in enumerate(cubNumbers):
    sum_dig = 0
    while val > 0:
        sum_dig += val % 10
        val //= 10
    if sum_dig % 7 == 0:
        sumDiv7 += cubNumbers[ind]
print("Сумма кубов которых делится нацело на 7:", sumDiv7)
for m in cubNumbers:
    numbers.append(m + 17)
sumDiv7 = 0
for ind, val in enumerate(numbers):
    sum_dig = 0
    while val > 0:
        sum_dig += val % 10
        val //= 10
    if sum_dig % 7 == 0:
        sumDiv7 += numbers[ind]
print("Сумма кубов которых делится нацело на 7 с прибавкой 17:", sumDiv7)
