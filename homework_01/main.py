"""
Домашнее задание №1
Функции и структуры данных
"""


from asyncio import format_helpers


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    
    return [num ** 2 for num in numbers]

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(num):
    if num > 1:
        if num == 2: return True
        for n in range(2, num):
            if num % n == 0 and num != n:
                return False
        return True
    else:
        return False

def is_even(num):
    if num % 2 == 0:
        return True
    return False

def is_odd(num):
    if is_even(num):
        return False
    return True


def filter_numbers(numbers_list, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    if filter_type == PRIME:
        return list(filter(is_prime, numbers_list))
    if filter_type == ODD:
        return list(filter(is_odd, numbers_list))
    if filter_type == EVEN:
        return list(filter(is_even, numbers_list))
    else:
        return False