#Numeric Data Type --> int,float,complex along wwith boolean

#Input Formatting --> Accepting input from the user --> input()

#Accepting integer input from user
'''
age = input('Enter the Age:')           #By Default input() accepts any input as String
print(age)
print(type(age))
'''

#But, int(input()) --> will accept only Integers
'''
age = int(input('Enter the Age:'))
print(age)
print(type(age))

age = float(input('Enter the Age:'))
print(age)
print(type(age))
'''
#Accepting Group of Values 
'''
a = input('Enter your Name and Age:').split()    #By Default, split() has space
print(a)

#Space Separated Values
a = input('Enter your College Name and Location:' ).split()   #Now you enter spaces in output (User)
print(a)

#Comma Separated Values
a = input("Enter the Values:").split(',')
print(a)
'''

#List of Integers
'''
marks = list(map(int,input("Enter the values:").split(',')))
print(marks)
'''
#Now, We want to accept 2 values from user
'''
age,salary = map(int,input("Enter the values:").split())
print(age)
print(salary)
'''
'''
age,marks,salary = map(int,input("Enter your age,marks and salary:").split())
print(age,marks,salary)
'''

# Operators -->ArithmeticError Operators perform operations between values (Operands)
# 7 Types --> Arithmetic, Assignment, Comparison (Relationship), Membership, Identity, Logical, Bitwise

# Arithmetic Operators --> Arithmetic Operations ( + , - , * , / , // , % , ** )

# TASK --> Accept Integer input as length and breadth --> Find the Area of Rectangle
# Area = length * breadth
'''
length,breadth = map(int,input('Enter length and breadth of Rectangle: ').split())
area = length * breadth     # If we want to do it in less number of line, Then...print("Area = ", length * breadth)
print(area)
'''
# Assignment Operators --> Assign the values ( = , += , -= )
'''
a = 50
print(a)
#Now, Update the value
a = a + 5  # instead of this, we camn write, a += 5
print(a) 
b = 50
b += a   # b = b + a
print(b)
'''

# TASK --> Try *= , /= , //= , %= , **=

# Comparison Operators --> We Compare the values --> Always given Boolean Output
# (==)-> Equal to, (!=)-> Not Equal to, (<)-> Less than, (>)-> greater than, (<=)-> Less than or Equal to, (>=)-> Greater than or equal to


# Membership Operators --> in, not in --> It checks for existance of an object in a collection -->  Gives Boolean Output

# Logicsl Operators --> Logical Decision Making --> and, or , not

# Identity Operators --> id() - gives where it is stores --> is, is not




































                    











































