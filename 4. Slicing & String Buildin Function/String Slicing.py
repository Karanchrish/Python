# Program using String Slicing

String1 = "Program using Slicing in Python"

# Slice "using" using Positive index (start=9, stop=14, step=1)
print(String1[9:14:1])  # using

# Slice "using" using Negative index (start=-23, stop=-18, step=1)
print(String1[-23:-18:1])  # using

# Skipping start value (stop=8, step=1)
print(String1[:8:1])  # Program

# Skipping stop value (start=19, step=1)
print(String1[19::1])  # in Python

# Skipping both start and stop value (step=1)
print(String1[::])  # Program using Slicing in Python

# -----------------------------------------

# Palindrome Program using Slicing

S1 = "YourStringHere"
S1 = S1.casefold()

if S1[::-1] == S1:
    print(S1 + ' is a Palindrome')
else:
    print(S1 + ' is not a Palindrome')