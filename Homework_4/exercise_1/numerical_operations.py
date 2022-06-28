class numer_operation:
    
    def __init__(self):
        self.__int_a = None
        self.__int_b = None

    @property
    def int_a(self):
        return self.__int_a

    @int_a.setter
    def int_a(self, int_a):
        if int_a.isdigit():
            self.__int_a = int(int_a)
        else:
            print("Not a number!")
            
    @property
    def int_b(self):
        return self.__int_b

    @int_b.setter
    def int_b(self, int_b):
        if int_b.isdigit():
            self.__int_b = int(int_b)
        else:
            print("Not a number!")
            
    def addition(self):
        sum = self.__int_a + self.__int_b
        print(f"Сумма сложения чисел {self.__int_a} и {self.__int_b} = {sum}")
        
    def multiplication(self):
        sum = self.__int_a * self.__int_b
        print(f"Сумма умножения числа {self.__int_a} на {self.__int_b} = {sum}")
        
    def subtract(self):
        sum = self.__int_a - self.__int_b
        print(f"Сумма вычитания чисел {self.__int_a} и {self.__int_b} = {sum}")
        
    def divide(self):
        if self.__int_a == 0 or self.__int_b == 0:
            print("Cant divide by zero")
        else:
            sum = self.__int_a / self.__int_b
            print(f"Результат деления чисел {self.__int_a} и {self.__int_b} = {sum}")
        
    def exponentiation_a_b(self):
        sum = self.__int_a ** self.__int_b
        print(f"Возведение числа {self.__int_a} в степень {self.__int_b} = {sum}")
    
    def exponentiation_b_a(self):
        sum = self.__int_b ** self.__int_a
        print(f"Возведение числа {self.__int_b} в степень {self.__int_a} = {sum}")
        
    def call_all_operation(self):
        self.addition()
        self.subtract()
        self.multiplication()
        self.divide()
        self.exponentiation_a_b()
        self.exponentiation_b_a()