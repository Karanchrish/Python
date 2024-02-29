my_dict = {'Name': 'xyz', 'Rollno': '123', 'Dept': 'AD', 'Age': 4}

# Modifying a value
my_dict['Name'] = 'xxyyzz'
print(my_dict)
#  {'Name': 'xxyyzz', 'Rollno': '123', 'Dept': 'AD', 'Age': 4}

# Adding a new key-value pair
my_dict['Phone no'] = 1234567890
print(my_dict)
#  {'Name': 'xxyyzz', 'Rollno': '123', 'Dept': 'AD', 'Age': 4, 'Phone no': 1234567890}

# Iterating keys
for i in my_dict:
    print(i)
# Name
# Rollno
# Dept
# Age
# Phone no

# Iterating values
for i in my_dict:
    print(my_dict[i])
# xxyyzz
# 123
# AD
# 4
# 1234567890

# Iterating values using dict.values()
for i in my_dict.values():
    print(i)
# xxyyzz
# 123
# AD
# 4
# 1234567890

# Iterating both keys and values
for i, j in my_dict.items():
    print(i, j)
# Name xxyyzz
# Rollno 123
# Dept AD
# Age 4
# Phone no 1234567890
