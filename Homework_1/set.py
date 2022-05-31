#1. Объявите и инициализируйте множество тремя различными способами
#1
set1 = {"t", "e"}
print(set1)
#2
list1 = ["r", "t"]
set2 = set(list1)
tuple1 = ("a", "f")
set3 = set(tuple1)
print(set2)
print(set3)
#3
set4 = set("q")
print(set4)
#4 почему бы и нет? 
set5 = frozenset('x')
print(set5)

#2. Удалите элемент из множества
set_del = {"test", "del"}
set_del.discard("test")
print(set_del)

#3 Удалите повторяющиеся элементы из списка
list_set = ["test", "duplicate", "duplicate"]
print(list(set(list_set)))

#4 Напишите скрипт, определяющий длину множества двумя различными способами.
set_length = {"test", "length", "3"}
print(len(set_length))
length = 0   
for i in set_length: 
    length += 1
print(length)

#5 Напишите скрипт для проверки, входит ли элемент в множество.
set_count = {"test", "count", "elem"}
print("test" in set_count)
print("duplicate" in set_count)