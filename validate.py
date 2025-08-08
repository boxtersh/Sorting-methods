def __check_type_list(array):

    assert isinstance(array, list), f'Ожидался класс: list, получили: {type(array)} '


def __check_type_str(line):

    assert isinstance(line, str), f'Ожидался класс: str, получили: {type(line)} '