#1. Вычислите сумму элементов (чисел) в списке двумя разными спосо­бами.
def sum_elem_list(lst):
    if not isinstance(lst, list):
        raise Exception("Переданный параметр не соответствует типу list")
    return sum([x for x in lst if isinstance(x, (float, int))])

#2. Умножьте каждый элемент списка на произвольное число.
def multiplication_elem_list(lst, multiplier):
    if not isinstance(lst, list):
        raise Exception("Переданный параметр не соответствует типу list")
    return [x * multiplier for x in lst if isinstance(x, (float, int))]

#3. Напишите скрипт для слияния (конкатенации) двух списков тремя различ­ными способами.
def merge_list(list1, list2):
    if not isinstance(list1 and list2, list):
        raise Exception("Переданный параметр не соответствует типу list")
    return list1 + list2

#4. Напишите скрипт, меняющий позициями элементы списка с индек­сами n и n+1
def changing_position_list_items_by_index(lst, index):
    if not isinstance(lst, list):
        raise Exception("Переданный параметр не соответствует типу list")
    if index >= len(lst):
        raise Exception("Переданный индекс в листе отсутствует")

    if index == len(lst)-1:
        lst[index], lst[index+1] = lst[index+1], lst[index]
    else:
        lst[index], lst[index+1] = lst[index+1], lst[index]

    return lst

#5. Напишите скрипт, переводящий список из различного количества числовых целочисленных элементов 
# в одно число. Пример списка: [1, 23, 456], результат: 123456  
def converting_list_to_integer(lst):
    if not isinstance(lst, list):
        raise Exception("Переданный параметр не соответствует типу list")
    return int("".join(map(str, lst)))

#3 Удалите повторяющиеся элементы из списка
def removing_duplicates_from_set(lst):
    if not isinstance(lst, list):
        raise Exception("Переданный параметр lst не соответствует типу list")
    return list(set(lst))