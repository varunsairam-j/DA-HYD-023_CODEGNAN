# Variable length arguments --> (*args)

# Variable length arguments --> The Number of positional arguments are not limited. We can pass any number of positional arguments
# But, we need to use the * representation, Data is stored in tuple
'''

def sample(*args):
    """Simple demo for *args"""
    print(args)
    print(type(args))

sample()                          # No Arguments
sample(1,2,3,4)                   # Any Number
sample('codegnan','varun',21)
details = [24,45,35,65]
sample(details)                   # passing a Collection
sample(*details)                  # unpacking values from collection

'''

'''
# * is used for unpacking the values from a collection
a,b,c = 13,4,'da'
print(a,b,c)

# a,*b,c = 'python',,'codegnan',23,45,9.7,'data'
# a,b,*c = 'python',,'codegnan',23,45,9.7,'data'

a,b,*c = 34,'codegnan'

print(a)
print(b)
print(c)
c.extend([23,45,6,7])
print(c)

'''

# TASK --> we wanted to caluculate the sum of given objects using Function

'''
def sum(*a):
    "Sum of Objects"
    total = 0
    for num in a:
        if type(num) == str:         # or type(num) in (int,float,complex) 
            total = total
        else:
            total += num
    return total
    
print(sum(1,2,3,4,2+7j,5,'code','gnan',6,7,8,9))

              #or

def add(*a):
    """sum of given objects"""
    print(a)
    print(type(a))
    #take output variable as result
    result=0
    for i in a:
        #print(i)
        #if type(i)==int or type(i)== float or type(i) == complex:
         if type(i) in (int,float,complex):
            result=result+i
    return result
#print(add())
#print(add(12,3,4,5))
#print(add(1,2,3,4.5))
#print(add(20,24,25))
print(add(3,4,5,'poll','dear',4.5))
print(add(23,4,5.5,2+4j,56,'code',23))
b=list(map(int,input("Enter the values:").split(',')))
# print(add(*b))          # * is used to unpack the values

# print(b)
#print(*b)         # it returns each value side by side

for i in b:
    print(i,end=' ')   #same as here

'''

# Keyword Variable length arguments --> we can pass any number of keyword arguments. we use ** representation

'''
def details (**kwargs):
    """Usage of **kwargs demo"""
    print(kwargs)
    print(kwargs.keys())
    print(type(kwargs))

details()           # returns empty dictionary
#details(2,3,4,5)   # raises Type error

details(name='codegnan',place='hyd',batch='da')
batch = {'number':'da23','place':'hyd'}
details(**batch)

'''

# Now let us include both of them into a function
'''
def sample(*a,**b):
    """Usage of both Variable length and keyword variable length argument"""
    result = 0
    for i in a:
        if type(i) in (int,float,complex):
            result += i
    print(result)
    for key,value in b.items():
        print(f'key is {key}')
        print(f'value is {value}')

sample(2,4,5,'police','codegnan',3.5,
       name="codegnan",
       place="hyd",
       batch="da23")
'''

# sample(name="codegnan",23,ids=23445)    # Positional args follows keyword args

































