a = {'name', 165, 'place', 9.5}

# Iterating through elements in the set
for i in a:
    print(i)
# 9.5
# 165
# place

# Adding elements to the set
a.add('b')
print(a)
# {'b', 'place', 9.5, 165}

a.update(['AD', '200'])
print(a)
# {'place', '200', 'b', 'AD', 'name', 9.5, 165}

# Removing elements from the set
a.remove(165)
print(a)
# {'place', '200', 'b', 'AD', 'name', 9.5}

a.discard('200')
print(a)
# {'place', 'b', 'AD', 'name', 9.5}

a.pop()
print(a)
# {'b', 'AD', 'name', 9.5}

# ----------------------------------

set1 = {1, 4, 5, 7, 3, 9, 0, 3, 6, 3}
temp = False
n = 7
for i in set1:
    if i == n:
        temp = True

if temp:
    print('yes')
else:
    print('No')

# -----------------------------------

a = {1, 2, 3, 4, 5, 6, 7, 8}
b = {2, 4, 6, 8, 10}

# Set union
print(a | b)
#  {1, 2, 3, 4, 5, 6, 7, 8, 10}

# Set difference
print(a - b)
#  {1, 3, 5, 7}

# Set intersection
print(a & b)
#  {2, 4, 6, 8}

# Symmetric difference
print(a ^ b)
#  {1, 3, 5, 7, 10}