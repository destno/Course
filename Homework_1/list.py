#1. Вычислите сумму элементов (чисел) в списке двумя разными спосо­бами.
str = list(input("Введите числа для подсчета их суммы через пробел или запятую: ").replace(",", " ").split())
num_list = []
for elem in str:
    if elem.isnumeric():
        num_list.append(int(elem))
theSum = 0
for i in num_list:
    theSum += i
print("Сумма чисел вычесленая первым способом: ", sum(num_list))
print("Сумма чисел вычесленая вторым способом: ", theSum)

#2. Умножьте каждый элемент списка на произвольное число.
str = list(map(int, input("Введите числа для их умножения через пробел или запятую: ").replace(",", " ").split()))
x = list(map(int,input("Введите число на которое будут умножены все числа в списке: ")))
for i in range(len(str)): 
    str[i] *= x
print(str)

#3. Напишите скрипт для слияния (конкатенации) двух списков тремя различ­ными способами.
list1 = input("Введите значения для первого списка разделяя пробелом или запятой: ").replace(",", " ").split()
list2 = input("Введите значения для второго списка разделяя пробелом или запятой: ").replace(",", " ").split()
#Способ первый
list3 = list1 + list2
#Способ второй
list1.extend(list2)
#Способ третий
for i in list2:
    list1.append(i)
#Способ четвертый
print([j for i in [list1, list2] for j in i])
#Способ пятый
print([*list1, *list2])

#4. Напишите скрипт, меняющий позициями элементы списка с индек­сами n и n+1
str = list(
        input(
            "Введите элементы для формирования листа разделяя пробелом или запятятую: "
        ).replace(",", " ").split()
    )
lenght = len(str)-1
ind = int(input(f"Введите номер индекса который поменять от 0 до {lenght}: "))
if ind <= lenght:
    if ind == lenght:
        str[ind], str[0] = str[0], str[ind]
        print("Был выбран последний элемент, смена произошла с первым элементом: ", str)
    else:
        str[ind], str[ind+1] = str[ind+1], str[ind]
        print("Элементы были изменены местами: ", str)
else:
    print("Выбраного элемента нету в списке")

#5. Напишите скрипт, переводящий список из различного количества числовых целочисленных элементов 
# в одно число. Пример списка: [1, 23, 456], результат: 123456  
str = list(
        input(
            "Введите элементы для формирования листа разделяя пробелом или запятятую: "
        ).replace(",", " ").split()
    )
print("".join(str))