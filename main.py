from random import randint as rnd
import time
import validate as vld
# ********************************** Модуль №5. Задание №3 ***************************************************
# ************  Задача №1. Сортировка “Пузырька” 10.79, 17.71 (с повтором) - [rnd(1,100) for _ in range(10000)]

def bubble_sorting_ascending_order(arr: list[int|float], order_by = lambda x, y: x > y,
                                                        key = lambda obj: obj )->list[int|float]:
    """
    Пример:
    [8,3,5,1],  []
    ответ:
    [1,3,5,8],  []
    :param arr: Массив для сортировки элементов
    :param order_by: условие сортировки (по возрастанию)
    :param key: ключ сортировки (сам объект)
    :return: отсортированный массив или пустой в случае передачи пустого массива
    """
    vld.__check_type_list(arr)
    len_arr = len(arr)
    if len_arr == 0: return []

    _start = time.time()

    for i in range(len_arr - 1):
        for j in range(len_arr - 1 - i):

            if order_by(key(arr[j]), key(arr[j+1])):
                arr[j], arr[j + 1] = arr[j+1], arr[j]

    end = time.time() - _start

    return arr


# ************  Задача №2. Сортировка выбором + подсчет операций 6.79, 13.22 (с повтором) - [rnd(1,100) for _ in range(10000)]

def sorting_permutations(arr: list[int|float], order_by = lambda x, y: x < y,
                                                    key = lambda obj: obj)->(list[int|float], int, int):
    vld.__check_type_list(arr)
    _start = time.time()
    len_arr = len(arr)
    count_compare = 0
    count_swap = 0

    for i in  range(len_arr - 1):
        max_i = i
        for j in range(i+1, len_arr):

            if order_by(key(arr[max_i]), key(arr[j])):
                max_i = j

            count_compare += 1

        if max_i != i:
            arr[i], arr[max_i] = arr[max_i], arr[i]
            count_swap += 1

    end = time.time() - _start
    return arr, count_compare, count_swap

# ************  Задача №3

def recursive_sum(array: list[int|float])->int|float:

    vld.__check_type_list(array)

    if not array:  return 0

    return array[0] + recursive_sum(array[1:])

# ************  Задача №4

def recursive_max(array: list[int|float])->int|float:

    vld.__check_type_list(array)

    if not array:  return 0

    if len(array) == 1: return array[0]

    max_elm = recursive_max(array[1:])

    return array[0] if array[0] > max_elm else max_elm

# ************  Задача №5

def recursive_sum_even_elem(array: list[int | float]) -> int | float:

    vld.__check_type_list(array)

    if not array: return 0

    if len(array) == 1: return array[0] if array[0] % 2 == 0 else 0


    return (array[0] if array[0] % 2 == 0 else 0) + recursive_sum_even_elem(array[1:])

# ************  Задача №6

def reverse_string(line: str) -> str:

    vld.__check_type_str(line)

    lnlin = len(line)

    if not line: return line

    if lnlin == 1: return line[0]

    return line[lnlin-1] + reverse_string(line[:lnlin-1])

# ************  Задача №7

def is_palindrome(line: str) -> bool:
    """
    Пример:
    лешанаполкеклопанашел -> True
    "12345" -> False

    :param line: Строка для проверки ее на палиндром
    :return: True если палиндром, иначе False
    """

    lnlin = len(line)

    if not line: return True

    if lnlin == 1: return True

    slice = line[1:lnlin-1]

    is_palindrome(slice)

    right_elm = slice[len(slice) - 1]
    left_elm = slice[0]

    return True if left_elm == right_elm else False



# print(is_palindrome('0123456789876543220'))




