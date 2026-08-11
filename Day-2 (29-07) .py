'''
Tokens --> Variables, Punctuators

Variables --> Named Memory Location
#Rules are to be Followed
'''
#MultiAssignment of Variables

'''
name,age,place = 'Varun','21','Hyderabad'
print(age,place,name)
print(age,place,name,sep=',')
'''

''''
a,b = 2,4,5 #Value Error as too many values
'''

#Re-assigning Variables

'''
name = "Varun"
a,b=4,8
print(a,b)
a,b=b,a
print(a,b,sep=',')
'''

'''
a,b = b,c #NameError as 'c' is not defined
print(a,b)
'''

#Deleting the Variables --> del
'''
del a
print(a)

del a,b
print(a,b)
'''

#Punctuators --> [],{},()

'''
Name = "Varun" ; Age = 21 ; Course = "Data Analytics"
print(Name,Course,Age)
print(Name,Course,Age,sep=' - ')
'''

#Data Types --> Numeric (int,float,complex),boolean,None
               #--> Sequences --> Lists,Tuples,Sets,Strings
               #    Frozen sets, mappings (dict)
'''
#Numeric Type --> int,float,complex
#int data type --> Quantity, Age.....

#print(type(a))

#float datatype --> temp,salary,price....

#complex -->combination of real and imaginary
'''

'''
i2 = 5
data = 5 + i2
print(data)   # This is not Imaginary (Complex)

data = 5+2j   #j is imaginary representation
print(data)
print(type(data))
'''

'''
age = 09
print(age)  #Should not start with zeroes for integers
'''
#But, We can start with zeroes for float

#Boolean --> True & False

'''
Value = True
Error = False
print(type(Value))
print(type(Error))
'''

#Type Casting --> Converting one type to another type

#Python by default follows Implicit Type (We need not to mention the datatype)

#We will go for Explicit Conversion

#Every Built-in data type is a built-in Function
#int,float,complex,bool

#Typecasting --> int -->float,complex,bool

'''
age = 21
print(type(age))
b = float(age)
print(b)
c = complex(age)
print(c)
d = bool(age)  #returns True for existing data
print(d)
e = bool(0)
print(e)
'''

#Float --> Type Casting -->int,complex,bool
'''
height = 6.2
print(type(height))
print(int(height))
print(complex(height))
print(bool(height))
'''

#complex -->Type Casting --> int,float,bool
'''
data = 2+5j
print(type(data))
#b = int(data)   #Type Error
#print(data)
#c = float(data)
print(c)
d = bool(data)
print(d)
print(type(d))

d = 5+4.5
print(d)
'''

'''
a = int(float(bool(100)))
print(a)
'''

#Combination of different Data Types
'''
z = 100 + 20.6 + 9 + 5j + False
print(z)
'''

# --> Explanation about Variables




























































