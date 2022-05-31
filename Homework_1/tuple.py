#1.Объявите и инициализируйте кортеж различными способами, после чего распакуйте его.
tuple1 = (1, 2, 3, 4)
tuple2 = tuple((1, 2))
a, b, c, d = tuple1
print(d, c, b, a)
e, f = tuple2
print(f, e)

#2 Конвертируйте список в кортеж, затем добавьте в кортеж новые элементы.
list1 = ['a', 'b', 'a', 'b']
tuple1 = tuple(list1)
tuple1 += (1,)
print(tuple1)

#3 Конвертируйте кортеж в словарь.
tuple1 = (('a', 'b'), ('1', '2'))
print(dict(tuple1))
print(dict(map(reversed, tuple1)))

#4 Напишите скрипт, подсчитывающий количество элементов типа кортеж в списке.
list1 = [('a', 'b'), ('1', '2'), 1,2]
i=0
for x in list1:
    if(isinstance(x, tuple)):
        i+=1
print("Количество элементов типа tuple в списке = ", i)
