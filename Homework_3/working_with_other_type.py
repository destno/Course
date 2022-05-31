#Добавьте еще несколько пар «ключ: значение» в следующий словарь: {0: 10, 1: 20}.
def adding_to_dict(dic, key, value):
    if not isinstance(dic, dict):
        raise Exception("Переданная словарь не соответствует типу dict")
    if not isinstance(key and value, (str, int)):
        raise Exception("Переданные ключ или значение не соответствуют типу str или int")
    if key in dic:
        raise Exception("Переданный key уже существует в словаре")
    dic[key] = value
    
    return dic

#2. Напишите скрипт, который из трех словарей создаст один новый.
def combining_dictionaries(dic1, dic2, dic3):
    if not isinstance(dic1 and dic2 and dic3, dict):
        raise Exception("Переданная словари не соответствует типу dict")
    return {**dic1, **dic2, **dic3} 

#3. Напишите скрипт для удаления элемента словаря.
def deleting_from_dict(dic1, key):
    if not isinstance(dic1, dict):
        raise Exception("Переданная словари не соответствует типу dict")
    if not key in dic1:
        raise Exception("Переданный ключ не входит в словарь")
    del dic1[key]
    return dic1

#4. Напишите скрипт, проверяющий, существует ли заданный ключ в словаре.
def exists_key_in_dict(dic1, key):
    if not isinstance(dic1, dict):
        raise Exception("Переданная словари не соответствует типу dict")
    return key in dic1

#1. Объявите и инициализируйте множество тремя различными способами
def create_set(lst):
    if not isinstance(lst, list):
        raise Exception("Переданный параметр не соответствует типу list")
    return set(lst)

#2. Удалите элемент из множества
def removing_elem_from_set(set1, elem):
    if not isinstance(set1, set):
        raise Exception("Переданный параметр set1 не соответствует типу set")
    if not isinstance(elem, (int, str)):
        raise Exception("Переданный параметр elem не соответствует типу int и str")
    if not elem in set1:
        raise Exception("Переданный элемент отсутствует во множесте")
    set1.discard(elem)
    return set1

#4 Напишите скрипт, определяющий длину множества двумя различными способами.
def lenght_set(set1):
    if not isinstance(set1, set):
        raise Exception("Переданный параметр set1 не соответствует типу set")
    return len(set1)

#5 Напишите скрипт для проверки, входит ли элемент в множество.
def exists_elem_in_set(set1, elem):
    if not isinstance(set1, set):
        raise Exception("Переданный параметр set1 не соответствует типу set")
    if not isinstance(elem, (int, str)):
        raise Exception("Переданный параметр elem не соответствует типу int или str")
    return elem in set1

#1.Объявите и инициализируйте кортеж различными способами, после чего распакуйте его.
def create_tuple(str1, str2):
    if not isinstance(str1 and str2, (str, int)):
        raise Exception("Переданныe параметры str1 или str2 не соответствует типу str или int")
    return tuple((str1, str2))

def unpacking_tuple(tupl):
    if not isinstance(tupl, tuple):
        raise Exception("Переданный параметр tupl не соответствует типу tuple")
    a, b = tupl
    return a, b

#2 Конвертируйте список в кортеж, затем добавьте в кортеж новые элементы.
def converting_list_to_tuple_and_add_elem(lst, elem):
    if not isinstance(lst, list):
        raise Exception("Переданный параметр lst не соответствует типу list")
    if not isinstance(elem, (int, str)):
        raise Exception("Переданный параметр elem не соответствует типу str или int")
    tuple1 = tuple(lst)
    tuple1 += (elem,)
    return tuple1

#3 Конвертируйте кортеж в словарь.
def converting_tuple_to_dict(tupl):
    if not isinstance(tupl, tuple):
        raise Exception("Переданный параметр tupl не соответствует типу tuple")
    return dict(tupl)

#4 Напишите скрипт, подсчитывающий количество элементов типа кортеж в списке.
def counting_elem_type_tuple(lst):
    if not isinstance(lst, list):
        raise Exception("Переданный параметр lst не соответствует типу list")
    return len([x for x in lst if isinstance(x, tuple)])
