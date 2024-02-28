#Program to check Leap Year or Not using Conditional Statements

year = int(input("Enter the Year : "))
if (year%4 == 0 & year%100 != 0 ):
          print(year,"is a Leap Year")
elif ( year%400 == 0 ):
          print(year,"is a Leap Year")
else:
          print(year,"is Not the Leap Year")

#--------------------------------------------

#program to find Sum of digits using Looping Statements

x=int(input("Enter the digits "))
sum=0
y=x
while(x>0):
  rem=x%10
  sum=sum+rem
  x=x//10
print("The sum of",y,"is",sum)

#--------------------------------------------

#Program to find a Fibanocci series using Looping Statements

a,b = 0,1
n = int(input("Enter the Number"))
print('The Fibonacci series are:')
for i in range(n):
  print(a,end = ' ')
  c = a+b
  a = b
  b = c

#--------------------------------------------

#Program to find a Factorial of a number using Looping Statements

num = int(input("Enter a number: "))
fact = 1
for i in range(1,num + 1):
       fact = fact*i
       print("The factorial of",num,"is",fact)

#--------------------------------------------

#Program to check the number is Odd or Even number using Looping and Conditional Statements

x=int(input('enter the lower value:'))
y=int(input('enter the upper value:'))
for i in range(x,y):
 if(i%2==0):
   print(i,"is even")
 else:
   print(i,"is odd")

#--------------------------------------------

# Program using Break and Continue

for i in range(10):
  if i == 8:
    break
  if i == 5:
    continue
  print(i)