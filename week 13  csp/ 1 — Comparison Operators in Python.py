# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment, while == is comparison.

a = 3
b = 4

print(a == b)   # False
print(a != b)   # True
print(a > b)    # False
print(a < b)    # True
print(a >= b)   # False
print(a <= b)   # True


#predict the output of the following comparisons:
10 > 5 #true
7 == 2 * 3 + 1 #true
8 != 8 #false
4 <= 2 + 2 #true

# Write 3 examples that result in True and 3 that result in False.
7 < 11 #true
8 == 4 * 2 #true
4 <= 4 #true
2 > 4 #False
10 == 5 * 3 #False
5 == 4 #False
# Create a simple grade-checking condition:
score = int(input("Enter your score: "))
if score >= 60:
    print("ayo you passed the test")
else:
    print("silly baka try better next time")
# practice problem :
# where a student must check if their score is greater than or equal to 60 to pass a test.# The password must be at least 8 characters long and contain at least one digit.password = "mypassword1"
password = input("Enter your password: ")
if len(password) >= 8 and any(char.isdigit() for char in password):
    print("goodjob your password is valid")
else:
    print(" ts fryin me son your password is invalid")4