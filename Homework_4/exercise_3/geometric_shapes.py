class shapes():
    
    def __init__(self, length_sides):
        self.__length_sides = length_sides
        self.__count_sides = len(length_sides)
        self.__perimetr = sum(self.length_sides)
        
    @property
    def length_sides(self):
        return self.__length_sides
    
    @property
    def count_sides(self):
        return self.__count_sides
    
    @property
    def perimeter(self):
        return self.__perimetr
    
class triangle(shapes):
    
    def __init__(self, length_sides):
        super().__init__(length_sides)
        self.__area = self.areas()
      
    def areas(self):
        a, b, c = self.length_sides
        p = (a+b+c)/2
        s = round((p*(p-a)*(p-b)*(p-c))**0.5, 4)
        return  s
    
    @property
    def area(self):
        return self.__area
    
    def __str__(self):
        return f"Длина сторон: {self.length_sides}, Количество сторон: {self.count_sides}, " \
                f"Периметр равен: {self.perimeter}, Площадь ровна: {self.area}"
                
class quadrangle(shapes):
    
    def __init__(self, length_sides):
        super().__init__(length_sides)
        self.__area = self.areas()
        
    def areas(self):
        a, b = self.length_sides[0:2]
        s = a*b
        return  s
    
    @property
    def area(self):
        return self.__area
    
    def __str__(self):
        return f"Длина сторон: {self.length_sides}, Количество сторон: {self.count_sides}, " \
                f"Периметр равен: {self.perimeter}, Площадь ровна: {self.area}"
                
class hexagon(shapes):
        
    def __init__(self, length_sides):
        super().__init__(length_sides)
        self.__area = self.areas()
        
    def areas(self):
        s = 3*(self.length_sides[0]**0.5)*self.length_sides[0]**2
        return  round(s, 4)
    
    @property
    def area(self):
        return self.__area
    
    def __str__(self):
        return f"Длина сторон: {self.length_sides}, Количество сторон: {self.count_sides}, " \
                f"Периметр равен: {self.perimeter}, Площадь ровна: {self.area}"  