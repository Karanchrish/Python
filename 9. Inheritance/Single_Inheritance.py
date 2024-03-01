# Single Inheritance
class Mobile:
  def __init__(self,brand,price):
    self.brand=brand
    self.price=price
  def buy(self):
    print("Buying a Mobile",self.brand,"worth of Rupees",self.price)
class Smartphone(Mobile):
    pass     
Vivo=Smartphone("Vivo",25000)
Vivo.buy()
Oppo=Smartphone("Oppo",15000)
Oppo.buy()
Redmi=Smartphone("Redmi",20000)
Redmi.buy()

''' 
Buying a Mobile Vivo worth of Rupees 25000
Buying a Mobile Oppo worth of Rupees 15000
Buying a Mobile Redmi worth of Rupees 20000
'''