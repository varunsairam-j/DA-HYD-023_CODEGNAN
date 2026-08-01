'''
# Integers are Immutable ( Their Storage Location does not Change ). where as,
# List is Mutable ( Their Location (id) doesn't change even if two lists have same values)
'''
'''
#Example -
a = [1,2,3,4]
b = [1,2,3,4]
print (a == b)  # Output is True, Because == compares the values in list
print (a is b)  # Output is False, Because their identity (location) is not same
'''

#Bitwise Operators --> We Perform Bitwise operations over operands
#--> & (and) , | (or) , ^ (XOR) , shifting operators ( << , >> )
# Numbers will be converted into Binary Format
'''
print (5&3) #Bitwise and
print (5|3) #Bitwise or
print (5^3) # Bitwise XOR
'''
#Left shift Operator ( << ) , Right shift Operator ( >> )
'''
print (5>>1) # The Binary Code for 5 is 0101. Here, we should shift the places to right. So, 0101 becomes 1010. Output is 10
'''

#Input Formatting --> input(), int9input)), float(input))
#We know Single Input
#2 or 3 Inputs --> map()
#group of integers --> list(map(int,input().split(','))


#Tokens --> Numeric Data Types --> Operators --> Flow of the Program
#Control Block Statements
#Conditional Statements --> if, else, elif (rely on condition to be executed)
#Repetion Statements (Loops) --> for, while


#Conditional Statements --> If & Else Statements
'''
Syntax -

if <condition>:
    statement(s)...
else:
    statement(s)...
'''


age = int(input("Enter Your Age:"))
if age>18:
    print("You are Eligible to Vote")
else:
<<<<<<< HEAD
    print(f"Your Age is : {age}. So, Your are not eligible to vote")  
=======
    print(f"Your Age is just:{age}. So, You are not Eligible to Vote")  
>>>>>>> 1a865bac02d876612a53fed7c150d9465ac4d596

# In Output, We are getting space after age. ( I don't want that ) --> ( Your Age is just: 12 So, You are not Eligible to Vote )
# So, There are methods for bringing output as we want 

'''
TASK - Student Marks and Grade Analyzer
90 - 100 = A
80 - 89 = B
70 - 79 = C
60 - 69 = D
>60 = Fail
Also, -ve cases should not be allowed and marks shouldn't be greater than 100
'''

































