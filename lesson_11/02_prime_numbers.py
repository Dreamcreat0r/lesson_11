# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


#def get_prime_numbers(n):
#    prime_numbers = []
#    for number in range(2, n+1):
#        for prime in prime_numbers:
#            if number % prime == 0:
#                break
#        else:
#            prime_numbers.append(number)
#    return prime_numbers

# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:
    # TODO здесь ваш код
    def __init__(self, n=100):
        self.n = n
        self.curr = 2
        self.primes = [2]
        pass

    def __iter__(self):
        self.curr = 2
        return self

    def __next__(self): 
        current = self.curr
        for self.curr in range(current+1, self.n+1):
            if self.curr >=self.n:
                raise StopIteration()
            for prime in self.primes:
                if self.curr % prime == 0:
                    break
            else:
                self.primes.append(self.curr)
                return self.curr

prime_number_iterator = PrimeNumbers(n=10000)
#for number in prime_number_iterator:
#    print(number)


# TODO после подтверждения части 1 преподователем, можно делать
# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_gen(n):
    # TODO здесь ваш код

    primes = []
    for number in range(2, n+1):
        for prime in primes:
            if number % prime == 0:
                break
        else:
            primes.append(number)
            yield number

#for number in prime_gen(n=10000):
#    print(number)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.

def happy_checker(n):
    n = str(n)
    leng = len(n)
    first = 0
    second = 0
    for ind in range(int(leng/2)):
        first += int(n[ind])
        second += int(n[leng-ind-1])
    if first == second:
        return int(n)


def prime_gen_v1(filter, n):
    primes = []
    for number in range(2, n+1):
        for prime in primes:
            if number % prime == 0:
                break
        else:
            if filter(number) != None:
                primes.append(number)
                yield number

#for number in prime_gen_v1(filter=happy_checker, n=10000):
#    print(number)

def prime_gen_v2(filter=None, filters=None, n=10):
    if filter != None:
        for number in prime_gen(n=n):
            if filter(number) != None:
                yield number

    elif filters != None:
        for number in prime_gen(n=n):
            for fil in filters:
                if fil(number) == None:
                    break
            else:
                yield number

def polyndrome_checker(n):
    n=str(n)
    rever = n[::-1]
    if n == rever:
        return n

for number in prime_gen_v2(filters=[polyndrome_checker, happy_checker], n=10000):
    print(number)