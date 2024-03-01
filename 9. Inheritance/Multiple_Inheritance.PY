#Multiple Inheritance
class Product:
  def __init__( self,brand,price):
    self.brand = brand
    self.price = price
  def buy(self):
    print(' Buying a moblie',self.brand,self.price)
class mobile(Product):
  def __init__(self,brand,price,ram):
      self.brand = brand
      self.price = price
      self.ram = ram
  def buy(self):
      print('Buying a smartphone ', self.brand,'Worth of Rs',self.price)
      print('ram :',self.ram)
class Smartphone(mobile,Product):
  def __init__(self,brand,price,ram,storage):
      super().__init__(brand,price,ram)
      self.storage = storage
  def buy(self):
    print('Buying a Smartphone', self.brand,'Worth  of Rupees',self.price)
    print('Ram :',self.ram,'and Storage :',self.storage)
Vivo=Smartphone("Vivo",25000,"16GB","128GB")
Vivo.buy()
Oppo=Smartphone("Oppo",15000,"8GB","64GB")
Oppo.buy()
Redmi=Smartphone("Redmi",20000,"8GB","128GB")
Redmi.buy()

''' 
Buying a Smartphone Vivo Worth  of Rupees 25000
Ram : 16GB and Storage : 128GB
Buying a Smartphone Oppo Worth  of Rupees 15000
Ram : 8GB and Storage : 64GB
Buying a Smartphone Redmi Worth  of Rupees 20000
Ram : 8GB and Storage : 128GB
'''