#Добавьте еще несколько пар «ключ: значение» в следующий словарь: {0: 10, 1: 20}.
dictin = {0: 10, 1: 20}
str = input("Введите несколько элементов для добавления в словарь разделяя пробелом или запятой: ").replace(",", " ").split()
for i in range(len(str)):
    x = i + 2
    dictin[x]=str[i]
print(dictin)

#2. Напишите скрипт, который из трех словарей создаст один новый.
def adddic(dictin):
    new_dic = {}
    for i in range(len(dictin)):
        new_dic[i]=[dictin[i]]
    return new_dic

str = "Введите несколько элементов для добавления их в(во) {} словарь разделяя пробелом или запятой: "
dic1 = adddic(list(input(str.format("первый")).replace(",", " ").split()))
dic2 = adddic(list(input(str.format("второй")).replace(",", " ").split()))
dic3 = adddic(list(input(str.format("третий")).replace(",", " ").split()))
for k, v in dic2.items():
    if k in dic1:
        dic1[k].extend(v)
    else:
        dic1[k] = v
for k, v in dic3.items():
    if k in dic1:
        dic1[k].extend(v)
    else:
        dic1[k] = v
print(dic1)

#3. Напишите скрипт для удаления элемента словаря.
def adddic(dictin):
    new_dic = {}
    for i in range(len(dictin)):
        new_dic[i]=dictin[i]
    return new_dic

dic1 = adddic(list(input("Введите несколько элементов для добавления их в первый словарь разделяя пробелом или запятой: ").replace(",", " ").split()))
elem = input(f"Введите номер элемента в виде числа от 0 до {max(dic1)}: ")
dic1.pop(int(elem), "Вы ввели несуществующий элемент")
print(dic1)

#4. Напишите скрипт, проверяющий, существует ли заданный ключ в словаре.
def adddic(dictin):
    new_dic = {}
    for i in range(len(dictin)):
        new_dic[i]=dictin[i]
    return new_dic

dic1 = adddic(list(input("Введите несколько элементов для добавления их в первый словарь разделяя пробелом или запятой: ").replace(",", " ").split()))
elem = input(f"Введите номер элемента в виде числа от 0 до {max(dic1)}: ")
if(int(elem) in dic1):
    print(f"Ключ в словаре присутсвует")
else:
    print("Ключ отсутсвует в словаре")