class MyClass:
  def __init__(self):
    self.public_attribute = "Public attribute"
    self.__private_attribute = "Private attribute"
    self._protected_attribute = "Protected attribute "
    
  
  def public_method(self):
    print('This is public method')
    
    
    
  def _private_method(self):
    print('This is private method')
    
  
  def _protected_method(self):
    print('This is protected method')
    
    
    
obj = MyClass()
print(obj.public_attribute)
obj.public_method()

print(obj._protected_attribute)
obj._private_method()