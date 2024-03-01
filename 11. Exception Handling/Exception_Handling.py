#Built in Exceptions
#Index Error
l=[1,2,3,4,5]
try:
  print(l[7]) 
except IndexError :
  print("list index out of range") # list index out of range

#Value Error
l=[1,2,3,4,5]
try:
  l.remove(7)
  print(l)
except ValueError:
   print("Value Error Founded")  # Value Error Founded

#Zero Division Error
n=int(input())
for i in range(n):
  try:
    a,b=input().split()
    print(int(a)/int(b))
  except ZeroDivisionError:
    print("Can't Divide by Zero, Try Again")
  except ValueError :
    print("Integers Only Allowed")

'''
3
study
Integers Only Allowed
1 0
Can't Divide by Zero, Try Again
1 1
1.0
'''

#Module Not Found Error
try :
  import Keylists
except ModuleNotFoundError :
  print("No module named 'Keylists'") # No module named 'Keylists'

#Key Error
a={'x':1,'y':2}
try:
  print(a['z'])
except KeyError:
  print("'z' not found") # 'z' not found

#User Defined Exception.
class Error(Exception):
  pass
class SalaryLowError(Error):
  pass
class SalaryHighError(Error):
  pass
Salary = int(input("Enter the Salary :"))
try:
  if Salary<0 :
    raise SalaryLowError
  elif Salary>100000 :
    raise SalaryHighError
except SalaryLowError :
  print("Enter the Valid Salary")
except SalaryHighError :
  print("Your Entered Salary is So High")

# Enter the Salary :-10000
# Enter the Valid Salary