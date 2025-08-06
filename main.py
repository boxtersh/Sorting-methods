from random import randint as rnd
import time
# ********************************** Модуль №5. Задание №3 ***************************************************
# Задача №1. Сортировка “Пузырька” 10.79, 17.71 (с повтором) - [rnd(1,100) for _ in range(10000)]
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
bubble_sorting(4)


