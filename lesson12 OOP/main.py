# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show_info(self):
#         print(f"Cat name '{self.name}' have age {self.age} years.")

# cat1 = Cat("Мурзик", 3)
# cat1.show_info()  

# cat2 = Cat("Барсік", 2)
# cat2.show_info() 






# class Student:
#     def __init__(self, name, course):
#         self.name = name
#         self.course = course
#         self.subjects = []

#     def add_subject(self, subject):
#         self.subjects.append(subject)

# student1 = Student("Іван", 2)
# student1.add_subject("Математика")
# student1.add_subject("Фізика")

# print(f"{student1.name} з {student1.course} курсу вивчає наступні предмети: {student1.subjects}")

# student2 = Student("Марія", 3)
# student2.add_subject("Історія")
# student2.add_subject("Хімія")
# student2.add_subject("Література")

# print(f"{student2.name} з {student2.course} курсу вивчає наступні предмети: {student2.subjects}")






# class Book:
#   def __init__(self, name, writer, year):
#     self.name = name
#     self.writer = writer
#     self.year = year
    
#   def __str__(self):
#     return f"Книга {self.name}, автор: {self.writer}, рік видання: {self.year}"
    
    
    
# book1 = Book("Гаррі Потер", "Джоан Кэ́тлин Роулинг", 1997)
# print(book1)

# book2 = Book("1984", "Джордж Орвелл", 1949)
# print(book2)





class PhoneDirectory:
  def __init__(self) -> None:
    self.contacts = {}
    
    
    
  def add_contact(self, name, number):
    self.contacts[name] = number
    
  def remove_contact(self, name):
    return self.contacts.pop(name)
  
  def get_phone_number(self, name):
    return self.contacts.get(name, "Контакт не знайдено.")
  
  
phone1 = PhoneDirectory()

phone1.add_contact("Іван", "123456789")
phone1.add_contact("Марія", "987654321")
phone1.add_contact("Петро", "555555555")


print(phone1.get_phone_number("Іван"))
print(phone1.get_phone_number("Марія"))
print(phone1.get_phone_number('Андрій'))
  
  
  

phone1.remove_contact("Іван")
print(phone1.get_phone_number("Іван"))