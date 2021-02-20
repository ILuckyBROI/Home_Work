#Реализовать склонение слова «процент» для чисел до 20.
# Например, задаем число 5 — получаем «5 процентов»,
# задаем число 2 — получаем «2 процента».Вывести все
# склонения для проверки
number = int(input('Введите число до 20: '))
i = 0
score = 0
if number == 0:
    print(number, '- процентов')
elif number == 1:
    print(number, '- процент')
elif number < 5:
    print(number, '- процентa')
else:
    print(number, '- процентов')
while i != 21:
    if i == 0:
        print(score, '- процентов')
        i += 1
        score += 1
    elif i == 1:
        print(score, '- процент')
        i += 1
        score += 1
    elif i < 5:
        print(score, '- процентa')
        i += 1
        score += 1
    elif i <= 20:
        print(score, '- процентов')
        i += 1
        score += 1
