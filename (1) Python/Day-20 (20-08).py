'''
Functions --> Arguments Usage (Variable length Arguments)
          --> Keyword Variable length arguments (**kwargs)
'''

# Exception Handling / Scope of Variables / Built-in Functions

# Exception Handling --> it is a Mechanism that helps to respond or malke the flow of excecution in a normal way. without this, Errors will
#                        occur and disrupt the program.


# Common Exceptions --> Value Error, Type Error, Index Error, Attribute Error, Zero division error

# Syntax:

''''
try:
    # Code will cause the Exception
except Exception as e:
    # Code will catch the Exception
finally:
    # runs irrespective of try/except
    ....
'''
 
# Basic Exception Handling
'''
try:
    #a =10
    a = int(input("Enter a Value:"))
    result = 20/a
    print(resul)
#except Exception as e:
    #print(e)             # it returns the msg of error

except ValueError:
    print('Invalid entry, enter only integer values')
except ZeroDivisionError:
    print(f'Division by Zero is not Possible')
except NameError:
    print(f'Check the name of Variable properly')
'''

'''
try:
    a = [1,2,3,4,5]
    for i in a:
        z = int(input("Enter Index Position:"))
        print(a[z])
except IndexError:
    print("Index is out of range")
'''

# Similarly if we want to check other Errors --> IndexError, AttributeError
# Multiple Exception Handling

'''
try:
    a = [10,20,30]
    a.apped(40)
    print(a[5])
#except Exception as e:
    #print(e)              #returns the message of error
except IndexError:
    print("Check the Length of list properly and access the elements")
except AttributeError:
    print("Don't rush, write the name properly")
except TypeError:
    print("Check the Spellings Properly")
'''
'''
try:
    a = [10,20,30]
    a.apped(40)
    print(a[5])
#except Exception as e:
    #print(e)              #returns the message of error
except (IndexError,AttributeError) as e:
    print(e)
    a  = list(map(int,input("Enter:").split(',')))         # just for understanding
    print(a)
'''

# BMI --> bmi = (weight) / (height)**2
# Feet --> 12 Inches. 1 Inch --> 2.54 Cm
'''
while True:
    try:
        weight = int(input("Enter the Weight in Kgs:"))
        height = int(input("Enter the Height in Meters:"))
        # write my logical condition
        if weight > 0 and height > 0:
            #break                          # stops the flow of excecution
            continue                        # skips the current iteration and proceed for remaining iterations
            #print("Bye")
        else:
            print("Make sure to enter only correct values")
    except ValueError:
        print("Make sure to enter weight in integer only, height also as number")
bmi = ((weight)/(height)**2)
print(bmi)

'''

# Use Exception Handling along with Jumping Statement in Functions

# Scope of Variables --> Scope is basically the region/area where it is accessible

# Local Scope, Global Scope
# Global Keyword, Enclosing Scope (Nested Functions Non Local Keyword)


# Local Scope --> Variables defined inside the function, accessible inside 

'''
def display():
    """Usage of Local Scope"""
    name = "Codegnan"
    print(name)
display()
#print(name)        # It raises NameError

'''
 
# Global Scope (Variables) --> Defined Outside and can be accessible anywhere in the script 

'''
place = 'Hyderabad'     # Global Variable
def display():
    """Usage of Local & Global Scope"""
    name = "Codegnan"   # Local Variable
    print(name)
    print(f'{name} is in {place}')
display()
print(place)

'''

# Modifying global variables inside the function and accessible outside the function

'''
count = 20
def data():
    """Usage of global keyword"""
    global count
    count = count + 5
    print(f'Value inside function is {count}')
data()
print(f'Value outside function is {count}')

'''
'''
count = 20
def data():
    """Priority of local vs global variable"""
    count = 5        # local variable
    count = count + 5
    print(f'Value inside function is {count}')
data()
print(f'Value outside function is {count}')

'''

# Enclosing Scope (Nonlocal keyword)

'''
def outer():
    """Outer Function with local variable"""
    count = 5
    def inner():
        """Nested Function"""
        nonlocal count
        count = count + 10
        print(f'Value inside is {count}')
    inner()
    print(f'Value outside is {count}')
outer()

'''

# Built-in Functions --> variables Built-in Scope

'''
len = 54
print(len+4)

print(len('codegnan'))          # TypeError --> Never Ever use Builtin Function as Identifiers

'''


# Exception Handling, Scope of Variables






























