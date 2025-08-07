from random import randint as rnd
import time
# ********************************** Модуль №5. Задание №3 ***************************************************
# ************  Задача №1. Сортировка “Пузырька” 10.79, 17.71 (с повтором) - [rnd(1,100) for _ in range(10000)]
def __check_list_empty(arr):

    assert isinstance(arr, list), f'Ожидался класс: list, получили: {type(arr)} '


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
    __check_list_empty(arr)
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
    __check_list_empty(arr)
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

def recursive_sum(arr: list[int|float])->int|float:

    if not arr: return 0

    return arr[0] + recursive_sum(arr[1:])

# ************  Задача №4

def recursive_max(arr: list[int|float])->int|float:

    if not arr:  return 0

    if len(arr) == 1: return arr[0]

    max_elm = recursive_max(arr[1:])
    return arr[0] if arr[0] > max_elm else max_elm

# ************  Задача №5

def recursive_sum_even_elem(arr: list[int | float]) -> int | float:

    if not arr:  return 0

    return 0 + arr[0] if recursive_sum_even_elem(arr[1:]) % 2 == 0 else 0

print(recursive_sum_even_elem([2,2,2,2]))