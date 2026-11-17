'''
Tokens, Datatypes --> Control Flow Statements --> if,elif,else, for,while, break,continue...

Procedure Oriented Programming

'''

# Functions --> A Function is a block of code wich performs a Specific Task

# Its a Reusable group of statements where we define using "def" keyword

# Advantages --> Code Reusability, Code Maintainability, Ease of Debugging, Avoiding Code duplication, Modularity...

# Syntax -

'''
def fname (parameters):             Function Definition
    """Doc String"""
    statement(s)....
    ..........                      Function body
    return value(s).....
fname(args)                         Function Call

'''

# To Perform Sum of given objects

'''
def add(a,b):
    """Sum of Objects"""
    c = a+b
    return c
print(add(12,3))                  # Addition
print(add('code','gnan'))         # Concatenation
print(add([12,5],[12,34]))        # Merging

x,y = map(int,input("Enter the Values:").split(','))
print(x,y)
print(add(x,y))

'''

'''
def add(a,b):
    """Sum of Objects without return"""
    print(a+b)
    
add('code','gnan')
print(add(12,-34))          # it returns result along with None

'''

'''
name,age,salary = "Saketh",32,50000
# usage of return

def details():
    #return name,age,salary
    #return "codegnan"
    #return 23+34+45
    return               # it returns None as Output
print(details())

'''

# There are 5 Types of Arguments :

# --> Positional Arguments
# --> Default Arguments
# --> Keyword Arguments
# --> Variable length arguments (*args)
# --> keyword variable length arguments (**kwargs)


# Positional Arguments --> Number of Arguments in function definition should match with function call (Order has to be maintained)

'''
def details(name,place):
     """To store the details"""
     #name = "Codegnan"
     #place = "Hyderabad"
     #return name,place
     print(f'Name is {name}')
     print(f'Place is {place}')
print(details("Saketh","Codegnan"))
print(details("Sai","Vigaz"))
# print(details("Vigaz","Shyam"))    # raises Type erroe as only 2 arguments should be given

c,d = map(str,input("Enter the values:").split(','))
details(c,d)

'''

# Default Arguments --> We can make arguments as default but not first argument as default

'''
#def grocery(item,price=35):
#def grocery(item="cheese",price=100):             # we can also make all arguments default
#def grocery(item="Burger",price):              # Non Default always follows Default
    """usage of default arguments"""
    print(f'The Item is {item} and price is {price}')

grocery("Milk",30)
#grocery(32,"Milk")
grocery("Bread")        # By Default we have given price as 35
grocery()               # as both item and price as default arguments

'''

# keyword arguments --> Whenever we wanted to specify the name of the argument

'''
def employee(name,salary,role,place="Codegnan"):
    """keyword arguments usage"""
    print(f'Employee name is {name},role is {role} and salary is {salary},works in {place}')
employee("Sai",20000,"Admin")
employee(salary = 25000,role = "Frontdesk",name = "Asha")
employee("Akash",250000,"IT","Cognizant")

'''

'''
def sub(a,b):
    """sub"""
    c = a-b
    return c
       

a = 10
b = 5
if a>b:
    print(sub(a,*b))
    
'''




# Explanation of Functions


















