L1 = ['name', '123i2', 1232, 'Place', 'CGPA9.9', 'ABC']
print(L1) # ['name', '123i2', 1232, 'Place', 'CGPA9.9', 'ABC']

# Slice
# Slicing using Positive Index
print(L1[:3]) # ['name', '123i2', 1232]

# Slicing using Negative Index
print(L1[-4:-1]) # ['Place', 'CGPA9.9', 1232]

# Inserting Element
# append
L1.append(629168) 
print(L1) # ['name', '123i2', 1232, 'Place', 'CGPA9.9', 'ABC', 629168]

# Insert
L1.insert(0, 'AD')
print(L1) # ['AD', 'name', '123i2', 1232, 'Place', 'CGPA9.9', 'ABC', 629168]

# Extend
L2 = ['D-Department']
L2.extend(L1)
print(L2) # ['D-Department', 'AD', 'name', '123i2', 1232, 'Place', 'CGPA9.9', 'ABC', 629168]

# Deleting Elements
# Pop
L1.pop(0)
print(L1) # ['name', '123i2', 1232, 'Place', 'CGPA9.9', 'ABC', 629168]

L1.pop()
print(L1) # ['name', '123i2', 1232, 'Place', 'CGPA9.9', 'ABC']

# Remove
L1.remove('Place2')  # Assuming you want to remove 'Place2', but it's not in the original list

# Clear
L1.clear()
print(L1) # []

# List Operators
L2 = [2, 5, 4, 2, 6, 7]

# Reverse Sorting
L2.sort()
print(L2) # [2, 2, 4, 5, 6, 7]

# Sorting
L2.sort(reverse=True)
print(L2) # [7, 6, 5, 4, 2, 2]

# Reverse
L3 = [3, 6, 5, 2, 2, 4, 7]
L3.reverse()
print(L3) # [7, 4, 2, 2, 5, 6, 3]

# Count
print(L3.count(2)) # 3

# Index
print(L3.index(7)) # 0

# max()
print(max(L3)) # 7

# min
print(min(L3)) # 2

# sum
print(sum(L3)) # 29

# -------------------------------------------

#subtracting a list from another list
print('Name:R.S.Karan Chrish')
print('Roll No:717821i223')
list1=[1,2,3,4,5,6]
list2=[5,6,7,8,9,]
list3=[]
for i in list1:
  if i not in list2:
     if i not in list3:
      list3.append(i)
print(list3)

# -------------------------------------------

#Count and Print the Occurence of an element in list
l1=[1,2,3,4,5,6]
l2=[5,6,7,8,9]
l3=[]
for i in l1:
  for j in l2:
    if(i!=j):
      if i not in l3:
        l3.append(i)
print(l3)

# -------------------------------------------

# program for finding Odd or Even

l1=[9,8,7,6,5,4,3,2,1]
even=[]
odd=[]
for i in l1:
  if(i%2==0):
    odd.append(i)
  else:
    even.append(i)  
print(odd)
print(even) 