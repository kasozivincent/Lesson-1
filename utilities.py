from typing import List


def is_even(number: int) -> bool:
    if (number % 2 == 0):
        return True
    else:
        return False


def is_one_digit(number: int) -> bool:
    return number < 10


def is_odd(number: int) -> bool:
    if (number % 2 == 1):
        return True
    else:
        return False


def get_last_digit(number: int) -> int:
    return number % 10


def max(a: int, b: int):
    return a if a >= b else b


def number_of_rows(matrix: List[List[int]]) -> int:
    return len(matrix)


def columns(matrix: List[List[int]]):
    return len(matrix[0])
