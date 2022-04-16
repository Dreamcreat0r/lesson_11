# -*- coding: utf-8 -*-

# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'

import path
import os.path



def log_errors(func):
    def modded(param):
        try:
            return func(param)
        except ValueError as exc:
            raise ValueError(f'Какая-то ошибка {exc}')
        except Exception as exc:
            raise Exception(f'Какая-то ошибка {exc}')
    return modded

    

# Проверить работу на следующих функциях
@log_errors
def perky(param):
    return param / 0



@log_errors
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')


#######################################################################################################################


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]


for line in lines:
    try:
        check_line(line)
    except Exception as exc:
        print(f'Invalid format: {exc}')


#perky(param=42)


# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла

def log_errors2(func, log_file):
    def modded(param):
        try:
            return func(param)
        except ValueError as exc:
            with open(log_file, 'a') as logs:
                logs.write(f'Произошла ошибка ValueError: {exc}\n')
        except Exception as exc:
            with open(log_file, 'a') as logs:
                logs.write(f'Произошла неизвестная ошибка {exc}\n')
    return modded


#@log_errors2('function_errors.log')      # По непонятной мне причине синтаксический сахар вида (@тратата) тут не работает,
#                                           поэтому переопредетяем функцию ручками. А так задача выполненеа
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')

check_line = log_errors2(check_line, 'function_errors.log')

for line in lines:
    check_line(line)
