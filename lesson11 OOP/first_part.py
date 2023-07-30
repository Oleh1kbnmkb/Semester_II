# class Person():
#   name = ''
#   age = 0
#   gender = ''
  
#   def sey_hello(self):
#     print(f'Hello, my name is {self.name}')
  
  
# person1 = Person()
# person1.name = 'Oleh'
# person1.age = 14
# person1.gender = 'Male'

# print(person1.__dict__)
# print(dir(person1))



# class Animal():
#   name = ''
#   age = 0
#   sound = ''
  
  
#   def say_animal(self):
#     print(f'Hello my name is {self.name}, my age {self.age} years and I say {self.sound}')
    
    
# animal1 = Animal()
# animal1.name = 'Cat'
# animal1.age = 3
# animal1.sound = 'meow'

# animal2 = Animal()
# animal2.name = 'Dog'
# animal2.age = 2
# animal2.sound = 'bark'

# print(animal1.__dict__)
# print(animal2.__dict__)

# animal1.say_animal()
# animal2.say_animal()




# class Car():
#   def __init__(self, brand, year, max_speed):
#     self.brand = brand
#     self.year = year
#     self.max_speed = max_speed
    
  
#   def get_max_speed(self):
#     return self.max_speed
  
  
#   def set_max_speed(self, new_max_speed):
#     self.max_speed = new_max_speed
    

# volvo = Car(brand='Volvo', year=2022, max_speed=260)
# print(volvo.get_max_speed())
# volvo.set_max_speed(310)
# print(volvo.get_max_speed())





class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.owner_name = name
        self.account_number = account_number
        self.balance = balance

    def add_money(self, amount):
        self.balance += amount
        print(f"На рахунок додано {amount} грн. Загальний баланс: {self.balance} грн.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"З рахунку знято {amount} грн. Загальний баланс: {self.balance} грн.")
        else:
            print("Недостатньо коштів на рахунку.")


account_1 = BankAccount(name="Ivan", account_number="123456789", balance=1000)


account_1.add_money(500)  
account_1.withdraw(200) 
account_1.withdraw(1500)
