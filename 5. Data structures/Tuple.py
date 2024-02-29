tuple1 = 'name', 13, 89, 'A D', 'Place', 13, 3
print(tuple1[0:2])  # ('name', 13)

# Positive index
print(tuple1[1])  # 13

# Negative index
print(tuple1[-1])  # 3

# Count the number
print(tuple1.count(13))  # 2

# Index value
print(tuple1.index(13))  # 1

tuple2 = 12, 23, 34, 45, 56

# Sum of the tuple
print(sum(tuple2))  # 170

# Maximum of the tuple
print(max(tuple2))  # 56

# Minimum of the tuple
print(min(tuple2))  # 12

tuple = (1, 2, 3, 4, 5, 6)
tuple[3] = 4
# Attempting to modify an element will raise an error
# Uncommenting the line below will result in a TypeError

# Tuple concatenation
tuple1 = 12, 34, 56
tuple2 = 98, 76, 54
tuple3 = tuple1 + tuple2
print(tuple3) # (12, 34, 56, 98, 76, 54)

# Repetition of the tuple
tuple_repeat = (1, 2) * 3
print(tuple_repeat) # (1, 2, 1, 2, 1, 2)

# Declare a nested tuple
nested_tuple = ((1, 2), (3, 4))
print(nested_tuple[1][0]) # 3

# Conversion of tuple to list
tuple1 = (10, 9, 5)
list1 = list(tuple1)
print(list1) # [10, 9, 5]

# Append method
list1.append(4)
print(list1) # [10, 9, 5, 4]

# Sorting the list
list1.sort()
print(list1) # [4, 5, 9, 10]

# Conversion of list back to tuple
tuple1 = tuple(list1)
print(tuple1) # (4, 5, 9, 10)

