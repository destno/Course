import pickle
import json

#1. Напишите скрипт для записи текста в файл.
with open("test_file.txt", "w") as file:
    file.write("test write")

#2. Напишите скрипт для чтения текста из файла.
with open("test_file.txt", "r") as file:
    print(file.read())

#3. Напишите скрипт для добавления текста в файл и отображения со­держимого файла.
with open("test_file.txt", "a+") as file:
    file.write("\nappend\nnew line\ntext\ntest")
    file.seek(0)
    print(file.read())

#4. Напишите скрипт для чтения последних п строк файла.
with open("test_file.txt", "r") as file:
    n = int(input("Введите количество последних строк для чтения: "))
    print(''.join(file.readlines()[-n:]))

#5. Напишите скрипт, подсчитывающий количество строк в файле.
with open("test_file.txt", "r") as file:
    i=0
    for line in file:
        i+=1
    print(i)

#6. Напишите скрипт, позволяющий найти самое встречаемое слово в файле.
with open("test_file.txt", "r") as file:
    text = file.read().split()
    print(dict((x, text.count(x)) for x in set(text) if text.count(x) > 1))

#7. Напишите скрипт, копирующий содержимое одного файла в другой.
with open("test_file.txt", "r") as output, open("copy_file.txt", "w+") as input:
    input.write(output.read())

#8. Запишите словарь в файл посредством модуля pickle и прочитайте его
dict1 = {1: 2, 2: 4, 3: 9, 4: 16}
with open("pickle_file", "wb") as file:
    pickle.dump(dict1, file)
    
with open("pickle_file", "rb") as file:
    print(pickle.load(file))

#9. Запишите список в файл посредством модуля pickle и прочитайте его.
list1 = ["b", [8, 4, 6], ['a']]
with open("pickle_file", "wb") as file:
    pickle.dump(list1, file)

with open("pickle_file", "rb") as file:
    print(pickle.load(file))

#10 Запишите словарь в файл посредством модуля json и прочитайте его.
dict1 = {1: 2, 2: 4, 3: 9, 4: 16}
with open("json_file.json", "w") as file:
    json.dump(dict1, file)

with open("json_file.json", "r") as file:
    print(json.load(file))