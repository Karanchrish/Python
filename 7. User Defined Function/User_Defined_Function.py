# Program using User Defined Function

def display(name, rollnumber, age=18):  # Function Definition
    print("My Name is", name, ", my Roll Number is", rollnumber, "And my age is", age)

name = input('Enter your name: ')
rollnumber = input('Enter your Roll number: ')
display(name, rollnumber)  # Function Calling

# Enter your name: John
# Enter your Roll number: 12345
# My Name is John , my Roll Number is 12345 And my age is 18

# Function to reverse a number
def reverse_number(num):
    # Convert the number to a string
    num_str = str(num)
    # Reverse the string
    reversed_str = num_str[::-1]
    # Convert the reversed string back to an integer
    reversed_num = int(reversed_str)
    return reversed_num

# Input: Enter a number
n = int(input('Enter a number: '))
# Call the function to reverse the number
result = reverse_number(n)
# Display the result
print(f'Reversed Number: {result}')

# Function Definition
def method():
    print("Function without arguments is done successfully")
# Function Calling
method() # Function without arguments is done successfully

# Function Definition
def method(name):
    print("My Name is", name)
# Function Calling
method('Karan') # My Name is Karan


#Function Definition
def method(name,age):
  print("My Name is ",name," and my age is ", age )
#Function Calling   
method(age=18,name="Karan") # My Name is  Karan  and my age is  18

def rep(list,n): 
#print("The repetition of the list elements is :",list*n) 
  x=list*n 
  x.sort() 
  for i in x: 
    print(i) 
list1=[] 
n=int(input("Enter the no of elements:")) 
for i in range(n): 
    x=int(input("Enter the element:")) 
    list1.append(x) 
y=int(input("Enter the no of times the list should be repeated:"))
rep(list1,y) 

# Enter the no of elements:3
# Enter the element:1
# Enter the element:2
# Enter the element:3
# Enter the no of times the list should be repeated:2
# 1
# 1
# 2
# 2
# 3
# 3

#function definition
def even_sum(List):
    Even_Sum = 0
    for j in range(n):
        if(List[j] % 2 == 0):
            Even_Sum = Even_Sum + List[j]
    return Even_Sum
#function definition
def odd_sum(List):
    Odd_Sum = 0
    for j in range(n):
        if(List[j] % 2 != 0):
            Odd_Sum = Odd_Sum + List[j]
    return Odd_Sum
 
List = []
n = int(input("Number of element "))
for i in range(1, n + 1):
    value = int(input("Enter element: "))
    List.append(value)
#function calling
Even_Sum = even_sum(List)
Odd_Sum = odd_sum(List)
print("The Sum of Even Numbers = ", Even_Sum)
print("The Sum of Odd Numbers = ", Odd_Sum)

# Number of element 5
# Enter element: 1
# Enter element: 3
# Enter element: 2
# Enter element: 5
# Enter element: 4
# The Sum of Even Numbers =  6
# The Sum of Odd Numbers =  9

#string mingling
s1 = "Karan" 
s2 = "Chrish" 
str = ""  
def collapse(str): 
 for i in s1: 
  for j in s2: 
   if s1.index(i) == s2.index(j): 
    s3 = i +j 
    str += s3 
 print(str) 
collapse(str) # KCahahrrahahns