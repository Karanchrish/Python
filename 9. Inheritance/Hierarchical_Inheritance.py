#Hierarchical Inheritance
class Mobile:
  def __init__(self,brand,price):
    self.brand=brand
    self.price=price
  def buy(self):
    print("Buying a Mobile",self.brand,"worth of Rupees",self.price)
class Smartphone(Mobile):
  def buy(self):
    print("Buying a Smartphone",self.brand,"worth of Rupees",self.price)  
class Keypadphone(Mobile):
  def buy(self):
    print("Buying a Keypadphone",self.brand,"worth of Rupees",self.price)      
Vivo=Smartphone("Vivo",25000)
Vivo.buy()
Oppo=Smartphone("Oppo",15000)
Oppo.buy()
Redmi=Smartphone("Redmi",20000)
Redmi.buy()
Jio=Keypadphone("Jio Mobile",1500)
Jio.buy()
Samsung=Keypadphone("Samsung",2500)
Samsung.buy()
Nokia=Keypadphone("Nokia Mobile",1000)
Nokia.buy()

'''
Buying a Smartphone Vivo worth of Rupees 25000
Buying a Smartphone Oppo worth of Rupees 15000
Buying a Smartphone Redmi worth of Rupees 20000
Buying a Keypadphone Jio Mobile worth of Rupees 1500
Buying a Keypadphone Samsung worth of Rupees 2500
Buying a Keypadphone Nokia Mobile worth of Rupees 1000
'''