#1. Напишите скрипт, вычисляющий двумя способами длину строки.
def find_length(string):
    if isinstance(string, (str, int)): 
        return len(string) 
    else: raise Exception("Переданный параметр не соответствует типу str или int")

#2. Напишите скрипт, который заменяет произвольный символ в строке на «$».
def symbol_replace(string, syb):
    if not isinstance(string, (str, int)):
        raise Exception("Переданная строка не соответствует типу str или int")
    if not isinstance(syb, int):
        raise Exception("Переданный символ не соответствует типу int")
    if not (syb <= len(string) and syb >= 0):
        raise Exception("Введен несуществующий символ")
    
    liststr = list(string)
    liststr[syb] = "$"
    return "".join(liststr)
        
#3. Напишите скрипт, который позволяет из строки собрать другую по следующим правилам: новая строка должна состоять из двух первых и двух последних элементов исходной строки. Если длина исходной строки меньше двух, то результатом будет пустая строка.
def builds_string(string):
    if not isinstance(string, (str)):
        raise Exception("Переданная строка не соответствует типу str")
    
    result = list(string)
    if(len(result) > 2):
        del result[2:len(result)-2]
    return ''.join(result)

#4. Напишите скрипт, который позволяет инвертировать последователь­ность элементов в строке.
def string_reversed(string):
    if not isinstance(string, (str)):
        raise Exception("Переданная строка не соответствует типу str")
    return string[::-1]


#5. Напишите скрипт, выводящий все элементы строки с их номерами индексов.
def get_index_symbol(string):
    if not isinstance(string, (str, int)):
        raise Exception("Переданная строка не соответствует типу str или int")
    for item in str(string):
        print(item, str(string).index(item))

#6. Поменяйте регистр элементов строки на противоположный.
def swap_case(string):
    if not isinstance(string, (str)):
        raise Exception("Переданная строка не соответствует типу str")
    return string.swapcase()

#7. Выведите символ, который встречается в строке чаще, чем остальные.
def repeating_element(string):
    if not isinstance(string, (str, int)):
        raise Exception("Переданная строка не соответствует типу str или int")
    result = sorted([(i,str(string).count(i)) for i in set(str(string))],key=lambda t:t[1])[-1]
    return f"Чаще всего встречается символ {result[0]}, он встречается {result[1]} раз(а)"
