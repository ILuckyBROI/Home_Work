#Реализовать вывод информации о промежутке времени в
#зависимости от его продолжительности duration в секундах:
#зависимости от его продолжительности duration в секундах:
#до минуты: <s> сек;v
#* до часа: <m> мин <s> сек;v
#* до суток: <h> час <m> мин <s> сек;v
#* *до месяца, до года, больше года: по аналогии.
duration = int(input('Введите число '))
d = (duration//86400) % 3600
h = (duration//3600) % 24
m = (duration//60) % 60
s = duration % 60
print('duration = ', duration)
print(d, 'дн', h, 'час', m, 'мин', s, 'сек')
#Есть баг при достижении 10 лет все начинается с начала как в
# проблеме 2000/2038 года) 311039999 End