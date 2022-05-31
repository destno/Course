'''
    1.  Напишите функцию, вычисляющую максимальное из трех чисел. Два вызова функции
'''

def max_int(num1, num2, num3):
    if all(isinstance(x, int) for x in [num1, num2, num3]):
        return max([num1, num2, num3])
    else:
        return "Не все параметры цифры"

print(max_int(1,2,5))
print(max_int(543,8321,12))

'''
    2. Напишите функцию, которая возвращает инвертированную строку, передаваемую ей на вход
'''

def reversed_string(str):
    return str[::-1]

print(reversed_string("test string"))

'''
    3. Напишите функцию для вычисления факториала задаваемого числа. Два вызова функции.
'''
def factorial(num):
    if isinstance(num, int): 
        if num == 0:
            return 1
        return factorial(num-1) * num
    else:
        return "Не верный формат ввода"

print(factorial(5))
print(factorial(10))

'''
    4. Напишите функцию, удаляющую повторяющиеся элементы в списке. Три вызова функции.
'''
def remove_dublicate_from_list(lis):
    if isinstance(lis, list):
        return list(set(lis))
    else:
        return "На вход подан не лист"

print(remove_dublicate_from_list(["etst", "test", "list", "test"]))
print(remove_dublicate_from_list(["3", "2", "1", "3"]))
print(remove_dublicate_from_list(["3", "3", "test", "test"]))

'''
    5. Напишите функцию, которая проверяет, является ли строка палин­дромом 
    (читается одинаково как слева направо, так и наоборот). 
    Два вызова функции (с палиндромом и нет).
'''

def palindrome(string):
    return string.upper() == string[::-1].upper()

print(palindrome("Level"))
print(palindrome("Up"))

'''
    6. Декорируйте функцию из первого упражнения таким образом, 
    чтобы возвращаемое ей значение возводилось в квадрат.
'''

def dec_max_int(func):
    def squaring(*args):
        res = func(*args)
        return res**2
    return squaring

@dec_max_int
def max_int(num1, num2, num3):
    if all(isinstance(x, int) for x in [num1, num2, num3]):
        return max([num1, num2, num3])
    else:
        return "Не все параметры цифры"

print(max_int(1,2,5))
print(max_int(543,8321,12))

'''
    7. Декорируйте функцию из 9 задания таким образом, чтобы возвращалась строка в верхнем регистре.
'''
def upper_case(func):
    def upper(*args):
        str = func(*args)
        return str.upper()
    return upper

@upper_case
def reversed_string(str):
    return str[::-1]

print(reversed_string("test string"))