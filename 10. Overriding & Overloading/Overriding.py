#Implementation of overriding
class Apparel:
  counter = 100
  def __init__(self,item_type):
    Apparel.counter +=1
    if(item_type.casefold() == 'cotton'):
      self.item_id = 'c'+str(Apparel.counter)
    elif(item_type.casefold() == 'silk'):
      self.item_id = 's'+str(Apparel.counter)
    self.price = None
    self.item_type = item_type
  def set_item_id(self,id):
    self.item_id=id
  def get_item_id(self):
    return self.item_id
  def set_price(self,price):
    self.price=price
  def get_price(self):
    return self.price
  def set_item_type(self,type):
    self.item_type=type
  def get_item_type(self):
    return self.item_type
  def calculate_price(self):
    #all apparel will have 1%tax
    tax =0.1*self.price
    return tax
class Cotton(Apparel):
  def __init__(self,price,discount):
    super().__init__("Cotton")
    self.price = price
    self.discount = discount
  #method overriding
  def calculate_price(self,discount):
    #cotton has 10% tax
    tax = super().calculate_price()
    self.price = tax + (self.price + (self.price *0.10))
  def display_bill(self):
    print('Hey there...you have purchased',self.item_type,self.item_id,'price is',self.price)
class Silk(Apparel):
  def __init__(self,price):
    super().__init__("Silk")
    self.price = price
    self.points=0
  #method overriding
  def calculate_price(self):
  #silk has 20% tax
   tax = super().calculate_price()
   self.price = tax + (self.price + (self.price *0.10))
  def display_bill(self):
     print('Hey there...you have purchased',self.item_type,self.item_id,'price is',self.price)
a = Cotton(1000,0.3)
a.calculate_price(3)
print(a.get_price(),a.item_type,a.item_id,Apparel.counter)
a.display_bill()
b = Silk(25000)
b.calculate_price()
print(b.get_price(),b.item_type,b.item_id,Apparel.counter)
b.display_bill()
a = Cotton(2000,0.3)
a.calculate_price(3)
print(a.get_price(),a.item_type,a.item_id,Apparel.counter)
a.display_bill() 
b = Silk(35000)
b.calculate_price()
print(b.get_price(),b.item_type,b.item_id,Apparel.counter)
b.display_bill()

'''
1200.0 Cotton c101 101
Hey there...you have purchased Cotton c101 price is 1200.0
30000.0 Silk s102 102
Hey there...you have purchased Silk s102 price is 30000.0
2400.0 Cotton c103 103
Hey there...you have purchased Cotton c103 price is 2400.0
42000.0 Silk s104 104
Hey there...you have purchased Silk s104 price is 42000.0
'''