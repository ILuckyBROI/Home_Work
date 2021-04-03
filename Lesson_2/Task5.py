#  Создать вручную список, содержащий цены на товары (10–20
#  товаров), например: 57.8, 46.51, 97, ...]
# A. Вывести на экран эти цены через запятую в одну строку, цена
# должна отображаться в виде <r> руб <kk> коп (например «5 руб 04
# коп»). Подумать, как из цены получить рубли и копейки, как
# добавить нули, если, например, получилось 7 копеек или 0 копеек
# (должно быть 07 коп или 00 коп).
# B. Вывести цены, отсортированные по возрастанию, новый список
# не создавать (доказать, что объект списка после сортировки
# остался тот же).
# C. Создать новый список, содержащий те же цены, но
# отсортированные по убыванию.
# D. Вывести цены пяти самых дорогих товаров. Сможете ли вывести
# цены этих товаров по возрастанию, написав минимум кода?

price = [57.8, 46.51, 97, 465, 89, 62.15, 71.99, 96.69, 32.06]
for i in price:
    rub, kop = str(f'{i:.2f}').split('.')
    print(f'{rub} руб {int(kop):02d} коп,', end=' ')
