import json

class notebook:
    
    def __init__(self):
        self.jotter = {}
 
    def addPerson(self):
        fio = input("ФИО: ")
        number = input("Номер телефона: ")
        birthdate = input("Дата рождения: ")
        email = input("Email: ")
        
        person = {"ФИО: ": fio, "Номер телефона: ": number,
                  "Дата рождения: ": birthdate, "Email: ": email}            

        try:
            with open("notebook.json", "r") as file:
                self.jotter = json.loads(file.read())
            with open("notebook.json", "w") as file:
                print(len(self.jotter))
                self.jotter[len(self.jotter) + 1] = person
        except FileNotFoundError:
            print("except")
            self.jotter["1"] = person
        finally:
            with open("notebook.json", "w") as file:        
                json.dump(self.jotter, file)
 
    def getPerson(self):          

        try:
            with open("notebook.json", "r") as file:
                self.jotter = json.loads(file.read())
            
            for item in self.jotter:
                print(self.jotter[item])
        except FileNotFoundError:
            print("Файла сохранений не существует, добавте новый контакт")
 
