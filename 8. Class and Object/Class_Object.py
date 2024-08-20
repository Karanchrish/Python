# Program using Class and Object

class student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.mark = []
        self.avg = 0

    def add_marks(self, m):
        self.mark.append(m)

    def cal_avg(self):
        for i in self.mark:
            self.avg += i
        self.avg = self.avg / len(self.mark)

    def display(self):
        print("Hi", self.name)
        print("Your roll number is", self.roll)
        print("Your marks are", self.mark)
        print("Your average is", self.avg)

# Creating instances of the student class
a = student("Karan Chrish", "717821I223")
a.add_marks(90)
a.add_marks(96)
a.add_marks(99)
a.add_marks(95)
a.add_marks(91)
a.cal_avg()
a.display()

b = student("Dhinesh", "717821I211")
b.add_marks(90)
b.add_marks(96)
b.add_marks(99)
b.add_marks(92)
b.add_marks(94)
b.cal_avg()
b.display()

c = student("Hari Hara Sudhanan", "717821I219")
c.add_marks(95)
c.add_marks(96)
c.add_marks(95)
c.add_marks(95)
c.add_marks(95)
c.cal_avg()
c.display()

d = student("Gubex", "717821I218")
d.add_marks(96)
d.add_marks(93)
d.add_marks(91)
d.add_marks(92)
d.add_marks(90)
d.cal_avg()
d.display()

e = student("Maki", "717821I228")
e.add_marks(94)
e.add_marks(93)
e.add_marks(94)
e.add_marks(91)
e.add_marks(93)
e.cal_avg()
e.display()

''' For student a (Karan Chrish):
Hi Karan Chrish
Your roll number is 717821I223
Your marks are [90, 96, 99, 95, 91]
Your average is 94.2

For student b (Dhinesh):
Hi Dhinesh
Your roll number is 717821I211
Your marks are [90, 96, 99, 92, 94]
Your average is 94.2

For student c (Hari Hara Sudhanan):
Hi Hari Hara Sudhanan
Your roll number is 717821I219
Your marks are [95, 96, 95, 95, 95]
Your average is 95.2

For student d (Gubex):
Hi Gubex
Your roll number is 717821I218
Your marks are [96, 93, 91, 92, 90]
Your average is 92.4

For student e (Maki):
Hi Maki
Your roll number is 717821I228
Your marks are [94, 93, 94, 91, 93]
Your average is 93.0 '''


class bank:
    def __init__(self, Holder_name, Account_number, IFSC):
        self.Holder_name = Holder_name
        self.Account_number = Account_number
        self.IFSC = IFSC
        self.Balance = 0

    def deposit(self, deposit_amount):
        self.deposit_amount = deposit_amount
        self.Balance = self.Balance + self.deposit_amount
        print("Now, Your Total Balance is : ", self.Balance)

    def withdraw(self, withdraw_amount):
        self.withdraw_amount = withdraw_amount
        if self.withdraw_amount <= self.Balance:
            print("You Have Sufficient Amount to Withdraw")
        else:
            print("Insufficient Amount")

    def checkbalance(self):
        if self.withdraw_amount <= self.Balance:
            print("Hi", self.Holder_name, "After Your Withdraw, Your Balance Amount is : ",
                  self.Balance - self.withdraw_amount)
        else:
            print("Hi", self.Holder_name, "After Your Withdraw, Your Balance Amount is : ", self.Balance)


Creating instances of the bank class
a = bank("Karan Chrish", "KCE717821I223", "KCE7178AIDS")
a.deposit(float(input("Enter the Amount to Deposit : ")))
a.withdraw(float(input("Enter the Amount to Withdraw : ")))
a.checkbalance()
print(" ")

b = bank("Dhinesh", "KCE717821I211", "KCE7178AIDS")
b.deposit(float(input("Enter the Amount to Deposit : ")))
b.withdraw(float(input("Enter the Amount to Withdraw : ")))
b.checkbalance()
print(" ")

c = bank("Hari Hara Sudhanan", "KCE717821I219", "KCE7178AIDS")
c.deposit(float(input("Enter the Amount to Deposit : ")))
c.withdraw(float(input("Enter the Amount to Withdraw : ")))
c.checkbalance()
print(" ")

d = bank("Maki", "KCE717821I228", "KCE7178AIDS")
d.deposit(float(input("Enter the Amount to Deposit : ")))
d.withdraw(float(input("Enter the Amount to Withdraw : ")))
d.checkbalance()
print(" ")

e = bank("Krishina", "KCE717821I226", "KCE7178AIDS")
e.deposit(float(input("Enter the Amount to Deposit : ")))
e.withdraw(float(input("Enter the Amount to Withdraw : ")))
e.checkbalance()

'''Creating instances of the bank class
For account holder a (Karan Chrish)
Enter the Amount to Deposit : 5000
Enter the Amount to Withdraw : 2000
You Have Sufficient Amount to Withdraw
Hi Karan Chrish After Your Withdraw, Your Balance Amount is : 3000

For account holder b (Dhinesh)
Enter the Amount to Deposit : 10000
Enter the Amount to Withdraw : 12000
Insufficient Amount
Hi Dhinesh After Your Withdraw, Your Balance Amount is : 10000

For account holder c (Hari Hara Sudhanan)
Enter the Amount to Deposit : 8000
Enter the Amount to Withdraw : 4000
You Have Sufficient Amount to Withdraw
Hi Hari Hara Sudhanan After Your Withdraw, Your Balance Amount is : 4000

For account holder d (Maki)
Enter the Amount to Deposit : 15000
Enter the Amount to Withdraw : 12000
You Have Sufficient Amount to Withdraw
Hi Maki After Your Withdraw, Your Balance Amount is : 3000

For account holder e (Krishina)
Enter the Amount to Deposit : 20000
Enter the Amount to Withdraw : 22000
Insufficient Amount
Hi Krishina After Your Withdraw, Your Balance Amount is : 20000 '''

class Flower:
    # Initial quantity and price of flowers
    q = {'orchid': 15, 'rose': 25, 'jasmine': 40}
    price = {'orchid': 1000, 'rose': 500, 'jasmine': 1200}

    def __init__(self, fn):
        # Initializing flower name, quantity, and price
        self.fn = fn.casefold()
        self.p = None
        self.sv = None

    def validate_flower(self):
        # Check if the requested flower is available
        if self.fn in self.q.keys():
            return True
        else:
            return False

    def validate_stock(self, required_quantity):
        # Check if the stock is sufficient for the requested quantity
        if required_quantity <= Flower.q[self.fn]:
            return True
        else:
            return False

    def sell_flower(self, required_quantity):
        # Sell the flower and update the stock
        if self.validate_stock(required_quantity) and self.validate_flower():
            Flower.q[self.fn] = Flower.q[self.fn] - required_quantity

    def calculate_price(self, required_quantity):
        # Calculate the total cost of the flowers
        return required_quantity * Flower.price[self.fn]


# Main program
print('Hello! Welcome to the flower shop!')
flower_name = input('Which flower do you wish to buy? : ')
f = Flower(flower_name)

if f.validate_flower():
    print('The requested flower is available.')
    required_quantity = int(input('Enter the required quantity: '))
    
    if f.validate_stock(required_quantity):
        p = f.calculate_price(required_quantity)
        print('Total cost is Rs.{}'.format(p))
        print('Thank you for shopping!')
        f.sell_flower(required_quantity)  # Update the stock after selling
    else:
        print('Stock unavailable.')
else:
    print('Sorry! Your request is unavailable.')

''' Hello! Welcome to the flower shop!
Which flower do you wish to buy? : rose
The requested flower is available.
Enter the required quantity: 10
Total cost is Rs.5000
Thank you for shopping! '''

class Hospital:
    # Constructor
    def __init__(self):
        self.bill_id = None
        self.patient_name = None
        self.bill_amt = None

    # Method to calculate bill amount
    def calculate_bill_amt(self, consultant_fees, quantity_list, price_list):
        self.bill_amt = consultant_fees + (quantity_list * price_list)
        print("The bill amount =", self.bill_amt)

    # Setter method for bill_id
    def set_billid(self, id):
        self.bill_id = id

    # Setter method for patient_name
    def set_patientname(self, name):
        self.patient_name = name

    # Getter method for bill_id
    def get_billid(self):
        return self.bill_id

    # Getter method for patient_name
    def get_patientname(self):
        return self.patient_name

# Main program
id = int(input("Enter the ID: "))
name = input("Enter Name: ")
bill = Hospital()

# Setting attributes using setter methods
bill.set_billid(id)
bill.set_patientname(name)

# Getting attributes using getter methods
print("Bill ID:", bill.get_billid())
print("Patient Name:", bill.get_patientname())

# User input for fees, quantity, and price
consultant_fees = int(input("Enter Fees: "))
quantity_list = int(input("Enter Quantity: "))
price_list = int(input("Enter Price: "))

# Calculating and displaying the bill amount
bill.calculate_bill_amt(consultant_fees, quantity_list, price_list)

''' Enter the ID: 123
Enter Name: John Doe
Bill ID: 123
Patient Name: John Doe
Enter Fees: 500
Enter Quantity: 2
Enter Price: 300
The bill amount = 1100 '''
