#Input
num1 = 5
num2 = 10

#Program using Arithemetic operation
#Addition
Addition = num1+num2
print('Addition of the Two Number is :',Addition) # 15, It Add num1 and num2

#Subtraction 
Subtraction = num1-num2
print("Subtraction of the Two Number is :",Subtraction) # -5, It Subtract num1 to num2

#multiplication
multiplication = num1*num2
print('multiplication of the Two Number is :',multiplication) # 50, It multiple num1 and num2

#Division
Division = num1/num2
print('Division of the Two Number is :',Division) # 0.5, It divides num1 to num2

#Floor Division
Floor_Division = num1//num2
print('Floor Division of the Two Number is :',Floor_Division) # 0, It avoids float values

#Modules
Modules = num1%num2
print('Modules of the Two Number is :',Modules) # 5, It gives remainder

#Exponential
Exponential = num1**num2
print("Exponential of the Two Number is :",Exponential) # 9765625, It gives its Power value

#---------------------------------------------------

#Program using Comparison (Relational) Operators

# Greater than
Greater = num1 > num2
print('Is', num1, '>', num2, ':', Greater) # True

# Lesser than
Lesser = num1 < num2
print('Is', num1, '<', num2, ':', Lesser) # False

# Greater than or equal to
Greater_equal = num1 >= num2
print('Is', num1, '>=', num2, ':', Greater_equal) # True

# Lesser than or equal to
Lesser_equal = num1 <= num2
print('Is', num1, '<=', num2, ':', Lesser_equal) # False

# Equal to
Equal = num1 == num2
print('Is', num1, '==', num2, ':', Equal) # False

# Not equal to
Not_equal = num1 != num2
print('Is', num1, '!=', num2, ':', Not_equal) # True

#---------------------------------------------------
#Program using Assignment Operators

# = (Assignment)
# = -> This is used to assign a value to a variable
result = 10

# += (Add and assign)
# += -> Adds a value to the current value of a variable and assigns the result to the same variable
result += 1

# -= (Subtract and assign)
# -= -> Subtracts a value from the current value of a variable and assigns the result to the same variable
result -= 2

# *= (Multiply and assign)
# *= -> Multiplies the current value of a variable by a value and assigns the result to the same variable
result *= 3

# /= (Divide and assign)
# /= -> Divides the current value of a variable by a value and assigns the result to the same variable
result /= 4

# //= (Floor divide and assign)
# //= -> Performs floor division on the current value of a variable by a value and assigns the result to the same variable
result //= 5

# %= (Modulus and assign)
# %= -> Calculates the modulus of the current value of a variable divided by a value and assigns the result to the same variable
result %= 6

# **= (Exponentiate and assign)
# **= -> Raises the current value of a variable to the power of a value and assigns the result to the same variable
result **= 2

#---------------------------------------------------

# Input
a = True
b = False

#Program using Logical Operators

# AND
print('a and b is:', a and b)  # Flase, Evaluates to True only if both a and b are True

# OR
print("a or b is:", a or b)   # True, Evaluates to True if at least one of a or b is True

# NOT
print('Not of a is:', not a)   # False, Evaluates to True if a is False
print('Not of b is:', not b)   # True, Evaluates to True if b is False

#---------------------------------------------------

# Program using Bitwise Operators

# Bitwise AND (&)
result_and = a & b  # Performs bitwise AND operation on corresponding bits of a and b
print('a and b is   :', result_and) # Flase

# Bitwise OR (|)
result_or = a | b   # Performs bitwise OR operation on corresponding bits of a and b
print("a or b is :", result_or) # True

# Bitwise XOR (^)
result_xor = a ^ b  # Performs bitwise XOR operation on corresponding bits of a and b
print("a xor b is :", result_xor) # True

# Bitwise NOT (~)
result_not_a = ~a  # Inverts the bits of a (bitwise NOT)
print('Not of a is :', result_not_a) # -2

# Left Shift (<<)
result_left_shift = a << 1  # Shifts the bits of a to the left by 1 position
print('Left shift of a is :', result_left_shift) # 2

# Right Shift (>>)
result_right_shift = a >> 1  # Shifts the bits of a to the right by 1 position
print('Right shift of a is :', result_right_shift) # 0

#---------------------------------------------------

# Program using Membership Operators

# in (True if value is found in the sequence)
sequence = [1, 2, 3, 4, 5]
value_in_sequence = 3
is_value_in_sequence = value_in_sequence in sequence
print(f'{value_in_sequence} in sequence : {is_value_in_sequence}') # True

# not in (True if value is not found in the sequence)
value_not_in_sequence = 6
is_value_not_in_sequence = value_not_in_sequence not in sequence
print(f'{value_not_in_sequence} not in sequence : {is_value_not_in_sequence}') # True

#---------------------------------------------------

# Program using Identity Operators

# is (True if both variables refer to the same object)
x = [1, 2, 3]
y = [1, 2, 3]
z = x

is_same_object_x_y = x is y
print('x is y:', is_same_object_x_y)  # False, as x and y are different objects with the same values

is_same_object_x_z = x is z
print('x is z:', is_same_object_x_z)  # True, as x and z refer to the same object

# is not (True if both variables do not refer to the same object)
is_not_same_object_x_y = x is not y
print('x is not y:', is_not_same_object_x_y)  # True, as x and y are different objects

is_not_same_object_x_z = x is not z
print('x is not z:', is_not_same_object_x_z)  # False, as x and z refer to the same object

#---------------------------------------------------

# Program using Ternary (Conditional) Operator
a = 10
b = 20

result = 'a is greater' if a > b else 'b is greater' # b is greater
print(result)
