class Vehicle:
    def __init__(self, brand, year) -> None:
        self.brand = brand
        self.year = year

    
    def drive(self):
        print("The vehicle is in motion.")

    
    def stop(self):
        print("The vehicle has stopped.")


class Car(Vehicle):
    def __init__(self, brand, year, fuel_type) -> None:
        super().__init__(brand, year)
        self.fuel_type = fuel_type

    
    def drive(self):
        print("The car is driving on the road.")
        
        
        
        
class Bicycle(Vehicle):
    def __init__(self, brand, year, color) -> None:
        super().__init__(brand, year)
        self.color = color

    
    def drive(self):
        print("The bike has been pedaled.")



car1 = Car('Toyota', 2021, 'Petrol')
car1.drive()
car1.stop()


bike1 = Bicycle('Titan', 2015, 'green')
bike1.drive()
bike1.stop()