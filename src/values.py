class int_value:
    """
    Дескриптор данных (данные числового типа). Вызывает исключение при неверном
    формате данных при присваивании.
    """

    def __init__(self, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if isinstance(value, int):
            instance.__dict__[self.__name] = value
        else:
            raise ValueError('Неверный тип данных (верный - int).')


class str_value:
    """
    Дескриптор данных (данные строкового типа). Вызывает исключение при неверном
    формате данных при присваивании.
    """

    def __init__(self, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if isinstance(value, str):
            instance.__dict__[self.__name] = value
        else:
            raise ValueError('Неверный тип данных (верный - str).')


class list_value:
    """
    Дескриптор данных (данные типа список). Вызывает исключение при неверном
    формате данных при присваивании.
    """

    def __init__(self, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if isinstance(value, list):
            instance.__dict__[self.__name] = value
        else:
            raise ValueError('Неверный тип данных (верный - list).')


class dict_value:
    """
    Дескриптор данных (данные типа словарь). Вызывает исключение при неверном
    формате данных при присваивании.
    """

    def __init__(self, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if isinstance(value, dict):
            instance.__dict__[self.__name] = value
        else:
            raise ValueError('Неверный тип данных (верный - dict).')


class bool_value:
    """
    Дескриптор данных (данные типа булево). Вызывает исключение при неверном
    формате данных при присваивании.
    """

    def __init__(self, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if isinstance(value, bool):
            instance.__dict__[self.__name] = value
        else:
            raise ValueError('Неверный тип данных (верный - bool).')
