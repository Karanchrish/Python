# Buildin Function

#abs()
print(abs(-45))    # 45
print(abs(-45.78))  # 45.78

#round
a = 13.7345
print(round(a))     # 14 (round to the nearest integer)
print(round(a, 2))   # 13.73 (round to 2 decimal places)

#all()
l1 = [0]
print('l1 =', all(l1))  # False (because there is a 0 in the list)

l2 = [1, 2, 3]
print('l2 =', all(l2))  # True (all elements are non-zero)

l3 = ["K", "A"]
print('l3 =', all(l3))  # True (all elements are truthy)

l4 = [1, 25 + 3j, 60]
print('l4 =', all(l4))  # True (all elements are truthy)

l5 = [1, 0 + 0j, 67]
print('l5 =', all(l5))  # False (because 0+0j is considered False)

l6 = [" ", "karan"]
print('l6 =', all(l6))  # True (all elements are truthy)

l7 = []
print('l7 =', all(l7))  # True (empty list, so all elements are considered True)

l8 = [False]
print('l8 =', all(l8))  # False (because there is a False in the list)

#any()
l1 = [0]
print('l1 =', any(l1))  # False (because all elements are falsy)

l2 = [1, 2, 3]
print('l2 =', any(l2))  # True (because at least one element is non-zero)

l3 = ["K", "A"]
print('l3 =', any(l3))  # True (because all elements are truthy)

l4 = [1, 25 + 3j, 60]
print('l4 =', any(l4))  # True (because all elements are truthy)

l5 = [1, 0 + 0j, 67]
print('l5 =', any(l5))  # True (because at least one element is non-zero)

l6 = [" ", "karan"]
print('l6 =', any(l6))  # True (because all elements are truthy)

l7 = []
print('l7 =', any(l7))  # False (because it's an empty list, and all elements are considered False)

l8 = [False]
print('l8 =', any(l8))  # False (because all elements are falsy)

l9 = [0 + 0j]
print('l9 =', any(l9))  # False (because all elements are falsy)

#ord
print(ord("K"))   # 75 (ASCII code for the uppercase letter 'K')

print(ord('k'))   # 107 (ASCII code for the lowercase letter 'k')

print(ord('0'))   # 48 (ASCII code for the digit '0')

print(ord('7'))   # 55 (ASCII code for the digit '7')

print(ord('.'))   # 46 (ASCII code for the dot/period '.')

print(ord('*'))   # 42 (ASCII code for the asterisk '*')

#chr
print(chr(75))   # 'K' (character corresponding to ASCII code 75)

print(chr(107))  # 'k' (character corresponding to ASCII code 107)

print(chr(48))   # '0' (character corresponding to ASCII code 48)

print(chr(55))   # '7' (character corresponding to ASCII code 55)

print(chr(46))   # '.' (character corresponding to ASCII code 46)

print(chr(42))   # '*' (character corresponding to ASCII code 42)

#ascii
print(ascii('karan'))     # "'karan'" (ASCII representation of the string 'karan')

print(ascii(223))         # '223' (ASCII representation of the integer 223)

print(ascii('*&^%$#@'))   # "'*&^%$#@'" (ASCII representation of the string '*&^%$#@')

print(ascii('诶'))        # "'\\u8bf6'" (ASCII representation of the Unicode character '诶')

print(ascii('கரன்'))     # "'\\u0b95\\u0bb0\\u0ba9\\u0bcd'" (ASCII representation of the string 'கரன்')

#bin
print(bin(10))   # '0b1010' (binary representation of the decimal number 10)

print(bin(-7))   # '-0b111' (binary representation of the negative decimal number 7)

#bool()
print(bool('karan'))   # True (non-empty string is truthy)

print(bool(0))         # False (integer 0 is falsy)

print(bool(" "))       # True (non-empty string is truthy)

print(bool(57))        # True (non-zero integer is truthy)

print(bool(9+4j))      # True (non-zero complex number is truthy)

print(bool(0+0j))      # False (zero complex number is falsy)

print(bool(False))     # False (Boolean value False is falsy)

#int
i = 223.223
i = int(i)
print(i, type(i))  # 223 <class 'int'>

#float
f = 223
f = float(f)
print(f, type(f))  # 223.0 <class 'float'>

#str
s = 3
s = str(s)
print(s, type(s))  # '3' <class 'str'>

s2 = True
s2 = str(s2)
print(s2, type(s2))  # 'True' <class 'str'>

#list
tup = (1, 2, 'karan')
tup = list(tup)
print(tup, type(tup))  # [1, 2, 'karan'] <class 'list'>

#tuple()
set_var = {1, 2, 'karan'}
set_var = tuple(set_var)
print(set_var, type(set_var))  # (1, 2, 'karan') <class 'tuple'>

# Removing Duplicate Elements by Converting to Set
a = [1, 2, 3, 4, 5, 3]
a = set(a)
print(a, type(a))  # {1, 2, 3, 4, 5} <class 'set'>

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#min
print(min(x))  # 1 (minimum value in the list)

#max
print(max(x))  # 9 (maximum value in the list)

#sum
print(sum(x))  # 45 (sum of all elements in the list)

#len
print(len(x))  # 9 (number of elements in the list)

#id
print(id(x))   # <id> (memory address of the list object)

#ISINSTANCE
print(isinstance(456, int))      # True (456 is an instance of the int class)
print(isinstance(456, float))    # False (456 is not an instance of the float class)
print(isinstance('karan', str))  # True ('karan' is an instance of the str class)

#FORMAT()
s = 'I am {name} from {clg}'.format(name='KC', clg='KCE')
print(s)  # 'I am KC from KCE'

#POW
print(pow(2, 3))  # 8 (2 raised to the power of 3)

#ITER() and NEXT()
l = ['K', 'a', 'r', 'a', 'n']
l_iterator = iter(l)
print(next(l_iterator))  # 'K' (first element of the list)
print(next(l_iterator))  # 'a' (second element of the list)
print(next(l_iterator))  # 'r' (third element of the list)
print(next(l_iterator))  # 'a' (fourth element of the list)
print(next(l_iterator))  # 'n' (fifth element of the list)
