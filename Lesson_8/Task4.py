# Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и выбрасывать
# исключение ValueError, если что-то не так, например:
# def val_checker...
#     ...
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5
# Примечание: сможете ли вы замаскировать работу декоратора?

def val_checker(l_func):
    def _val_checker(func):
        def wrapper(num):
            if l_func(num):
                print(func(num))
            else:
                raise ValueError(f'Wrong VAL {num}')

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


try:
    a = calc_cube(3)
except ValueError as Error:
    print(Error)