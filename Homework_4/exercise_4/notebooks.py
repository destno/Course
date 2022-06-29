import json
import os

from requests import JSONDecodeError

class notebook:
 
    def __init__(self):
        self.jotter = []
        
    def add_person(self):
        name = input("ФИО: ")
        number = input("Номер телефона: ")
        birthdate = input("Дата рождения: ")
        email = input("Email: ")
        
        file_name = input("Введите название файла для сохранение: ")
        
        person = {'name': name, 'phone_number': number,'birthdate': birthdate, 'Email': email}

        try:
            with open(f"{file_name}.json", "r") as file:
                person_file = json.loads(file.read())
                if len(person_file) != 0:
                    write_type = input("Введите 'a' для дозаписи, введите 'w' для перезаписи: ")
                    if write_type=="a":
                        for item in person_file:
                            self.jotter.append(person_file[item])
        except FileNotFoundError:
            pass
        except JSONDecodeError:
            pass
        finally:
            with open(f"{file_name}.json", "w") as file:
                self.jotter.append(person) 
                new_dict = {item['name']:item for item in self.jotter}
                json.dump(new_dict, file)
            self.jotter.clear()
            
    def get_person(self):          
        file_name = input("Введите название файла для загрузки: ")
        try:
            with open(f"{file_name}.json", "r") as file:
                person_file = json.loads(file.read())
            
            for item in person_file:
                print(person_file[item])
        except FileNotFoundError:
            print("Файла сохранений не существует, добавте новый контакт")
            
    def find_person(self):
        file_name = input("Введите название файла в котором произвести поиск контакта: ")
        find_name = input("Введите имя контакта для поиска: ")
        try:
            with open(f"{file_name}.json", "r") as file:
                person_file = json.loads(file.read())
            
            for item in person_file:
                if person_file[item]['name'] == find_name:
                    print(person_file[item])
        except FileNotFoundError:
            print("Файла сохранений не существует, добавте новый контакт")
            
    def del_person(self):
        file_name = input("Введите название файла в котором произвести удаление контакта: ")
        find_name = input("Введите имя контакта для удаления: ")
        try:
            with open(f"{file_name}.json", "r") as file:
                person_file = json.loads(file.read())
                for item in person_file:
                    self.jotter.append(person_file[item])
            
            for item in self.jotter:
                if item['name'] == find_name:
                    self.jotter.remove(item)
                    
            with open(f"{file_name}.json", "w") as file:
                new_dict = {item['name']:item for item in self.jotter}
                json.dump(new_dict, file)
        except FileNotFoundError:
            print("Файла сохранений не существует, добавте новый контакт")
        self.jotter.clear()
