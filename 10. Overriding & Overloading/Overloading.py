#Implementation of overloading
class Sample:
  def __init__(self,a,b):
    self.a = a
    self.b = b
  def __str__(self):
    return "{},{}".format(self.a,self.b)
#operator overloading
  def __add__(self,other):
    x = self.a + other.a
    y = self.b + other.b
    return Sample(x,y)
obj1 = Sample(7,5)
obj2 = Sample(5,9)
print(obj1+obj2)  # 12,14

#Implementation of overloading
class sample:
  def __init__(self,a,b):
    self.a=a
    self.b=b
  def __str__(self):
    return "{},{}".format(self.a,self.b)
  def __lt__(self,other):
    x=self.a > other.a
    y=self.b > other.b
    return sample( x,y)
s=sample(1,4)
r=sample(1,9)
print(s>r) # False,True

#Implementation of overloading
class sample:
  def __init__(self,a,b):
    self.a=a
    self.b=b
  def __str__(self):
    return "{},{}".format(self.a,self.b)
  def __add__(self,other):
    x=self.a + other.a
    y=self.b + other.b
    return sample( x,y)
  def __sub__(self,other):
    x=self.a - other.a
    y=self.b - other.b
    return sample( x,y)
  def __lt__(self,other):
    x=self.a > other.a
    y=self.b > other.b
    return sample( x,y)
s=sample(1,1)
r=sample(1,1)
o=sample(1,1)
print(s+r+o)
print(s-r-o)
print(s>r)

''' 
3,3
-1,-1
False,False
'''

#Implementation of overloading
class Sample:
  def __init__(self,a,b):
    self.a = a
    self.b = b
  def __str__(self):
    return "{},{}".format(self.a,self.b)
#operator overloading
  def __sub__(self,other):
    x = self.a - other.a
    y = self.b - other.b
    return Sample(x,y)
obj1 = Sample(8,9)
obj2 = Sample(7,3)
print(obj1-obj2) # 1,6