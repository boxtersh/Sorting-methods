def __check_type_list(array):

    assert isinstance(array, list), f'Ожидался класс: list, получили: {type(array)}'


def __check_type_str(line):

    assert isinstance(line, str), f'Ожидался класс: str, получили: {type(line)}'


def __check_type_int(n):

    assert isinstance(n, int), f'Ожидался класс: int, получили: {type(n)}'


def __check__number_positive(n):

    assert n >= 0, f'Ожидалось положительное число N, получили: {type(n)}'