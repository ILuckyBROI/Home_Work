# Создать собственный класс-исключение, который должен проверять содержимое списка на
# наличие только чисел. Проверить работу исключения на реальном примере. Запрашивать у
# пользователя данные и заполнять список необходимо только числами. Класс-исключение
# должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока
# пользователь сам не остановит работу скрипта, введя, например, команду «stop». При этом
# скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для этого задания примем, что пользователь может вводить только числа и
# строки. Во время ввода пользователем очередного элемента необходимо реализовать
# проверку типа элемента. Вносить его в список, только если введено число. Класс-исключение
# должен не позволить пользователю ввести текст (не число) и отобразить соответствующее
# сообщение. При этом работа скрипта не должна завершаться.

class Exception:
    def __init__(self, *args):
        self.info = []

    def in_info(self):
        while True:
            try:
                val = int(input('Введите значение для добавления в список: '))
                self.info.append(val)
                print(f'Текущий список:{self.info} \n ')
            except:
                print(f"Недопустимое значение - строка и булево")
                ext = input(f'Попробовать еще раз? Cont/Stop: ').lower()
                if ext == 'cont':
                    print(try_except.in_info())
                elif ext == 'stop':
                    return (f'Вы вышли. \nСозданый вами список:{self.info}')
                else:
                    return (f'Вы вышли. \nСозданый вами список:{self.info}')


try_except = Exception(1)
print(try_except.in_info())