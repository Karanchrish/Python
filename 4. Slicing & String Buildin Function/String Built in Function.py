# Program using String Builtin Function 
S1 = 'good morning'

# Using uppercase
print(S1.upper())  # GOOD MORNING

# Using lowercase
print(S1.lower())  # good morning

# Using title
print(S1.title())  # Good Morning

# Using casefold
print(S1.casefold())  # good morning

# Using capitalize
print(S1.capitalize())  # Good morning

# Using swapcase
print(S1.swapcase())  # GOOD MORNING

# Using count
print(S1.count('g'))  # 2

# Using find
print(S1.find('good'))  # 1
print(S1.find('god'))   # -1

# Using rfind
print(S1.rfind('good'))  # 1

# Using index
print(S1.index('morning'))  # 6

# Using replace
print(S1.replace('morning', 'evening'))  # good evening 

# Using center
print(S1.center(20, '-'))  # - good morning ---

# Using strip
print(S1.strip())  # good morning

# Using startswith
print(S1.startswith(''))  # True

# Using endswith
print(S1.endswith('g'))  # False

# Using rindex
print(S1.rindex('morning'))  # 6

# Program using isupper
print(S1.isupper())  # False

# Program using islower
print(S1.islower())  # True

# Program using istitle
print(S1.istitle())  # False

# Program using isalpha
print(S1.isalpha())  # False

# Program using isalnum
print(S1.isalnum())  # False

# Program using isdigit
print(S1.isdigit())  # False

# Program using split
S = S1.split()
print(S)  # Output: ['good', 'morning']

# Program using join
print('-'.join(S1))  # Output: g-o-o-d- -m-o-r-n-i-n-g-

# Using isupper
print(S1.isupper())  # False

# Using islower
print(S1.islower())  # True

# Using istitle
print(S1.istitle())  # False

# Using isalpha
print(S1.isalpha())  # False

# Using isalnum
print(S1.isalnum())  # False

# Using isdigit
print(S1.isdigit())  # False

# Using split
S = S1.split()
print(S)  # Output: ['good', 'morning']

# Using join
print('-'.join(S1))  # Output: g-o-o-d- -m-o-r-n-i-n-g-