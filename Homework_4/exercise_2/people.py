class person():
    
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property 
    def name(self):
        return self.__name
    
    @property        
    def age(self):
        return self.__age
    
    @property         
    def gender(self):
        return self.__gender
            
class teacher(person):
    
    def __init__(self, name, age, gender, experience, subject):
        super().__init__(name, age, gender)
        self.__experience = experience
        self.__subject = subject

    @property
    def subject(self):
        return self.__subject
 
    @property           
    def experience(self):
        return self.__experience
            
    def __str__(self):
        return f"Имя: {self.name}, Возвраст: {self.age}, Пол: {self.gender}, " \
                f"Предмет: {self.subject}, Стаж: {self.experience}"
            
class student(person):
    
    def __init__(self, name, age, gender, specialty, cource):
        super().__init__(name, age, gender)
        self.__specialty = specialty
        self.__course = cource

    @property
    def specialty(self):
        return self.__specialty
 
    @property           
    def course(self):
        return self.__course
            
    def __str__(self):
        return f"Имя: {self.name}, Возвраст: {self.age}, Пол: {self.gender}, " \
                f"Специальность: {self.specialty}, Курс: {self.course}"