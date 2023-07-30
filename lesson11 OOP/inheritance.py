# class Vehicle:
#   def __init__(self, brand, year) -> None:
#     self.brand = brand
#     self.year = year
    
  
  
#   def drive(self):
#     print('The vehicle is in motion.')
    
    
#   def stop(self):
#     print('The vehicle has stopped.')
    


# class Car(Vehicle):
#   def __init__(self, brand, year, fuel_type, color) -> None:
#     super().__init__(brand, year)
#     self.fuel_type = fuel_type
#     self.color = color
    
    
#   def drive(self):
#     print(f'The car is driving on the road.')
    
    
# car1 = Car('Toyota', 2021, 'Petrol', 'yellow')

# car1.drive()
# car1.stop()
    
    
    
    
    
# class Вісусlе(Vehicle):
#     def __init__(self, brand, year, fuel_type, color):
#         super().__init__(brand, year)
#         self.fuel_type = fuel_type
#         self.color = color

#     def drive(self):
#         print(f'The {self.color} Вісусlе is driving on the road.')


# visusle1 = Вісусlе("Toyota", 2022, "petrol", "red")
# visusle2 = Вісусlе("Honda", 2021, "diesel", "blue")


# visusle1.drive()
# visusle2.drive() 










class Shape:
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def perimeter(self):
        return 4 * self.side_length

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Створення об'єктів класів Square та Circle
square = Square(5)
circle = Circle(3)

# Обчислення периметрів та виведення результатів
square_perimeter = square.perimeter()
circle_perimeter = circle.perimeter()

print("Perimeter of the square:", square_perimeter)  # Виведе: Perimeter of the square: 20
print("Perimeter of the circle:", circle_perimeter)  # Виведе: Perimeter of the circle: 18.84
