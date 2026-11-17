# Mapping --> Dictionary --> Collection of Key-value pairs used to store related Data

# --> HSON, APIs, Database records

'''
dict() --> data = {} --> data = {key : value}

Dictionary is Mutable, Indexed through keys, Ordered, Heterogeneous and
Keys must be Unique (int,strings,float values...)

'''

details = {}
print(type(details))

details = {'Id' : 'CGH3937','Name' : 'Varun',
           'Gender' : 'M','Age' : 21,
           'Batch' : 'DA23','Place' : 'Hyd'}

print(details)
print(len(details))

# Accessing the Data from Dictionary
#print(details[])    #key Error

print(details.keys())      # It returns keys from the dictionary

print(details['Id'])     # return the value of that key

# if key name is not matching or if it is invalid - it returns key error

# print(details['marks'])      # key error as marks is not present

'''
details['marks'] = []
print(details)

print(type(details['marks']))

details['marks'].append(20)
print(details)

details['marks'].extend([10,20,30,40])
print(details)

# Create a key-value pair of Practice Session

details['Practice Session'] = ('Tuesday','Thrusday','Saturday')
print(details.keys())

# Accessing 3rd Day Marks of Student
print(details['marks'][2])

details['Mock Interviews'] = ('Monday','Wednesday','Friday')

# Operations --> Mutable, Indexing through keys, Membership

print('Wednesday' in details)      # returns False as that key is not present
print('Mock Interviews' in details)          # return True


for i in details:
    print(i)        # returns keys one by one

     #or

for i in details.keys():
    print(f'Key = {i}')
    print(f'Value = {details[i]}')



# keys() --> returns keys from the dictionary


for i in details.values():        # returns value from dictionary
    print(i)

for i in details.items():      # returns key-value pair in tuple
    print(i)

for key,value in details.items():
    print(f'key is {key}')
    print(f'value is {value}')

'''

# update() --> Updating the dictionary with key-value pairs

'''
details.update({'marks' : [],
                'PS': ('Tuesday','Thrusday','Saturday')})

print(details)
details['marks'].extend([25,30,35])
print(details)

marks = list(map(int,input("Enter the Marks:").split(',')))
print(marks)
details['marks'].extend(marks)
print(details)

'''

print(details.keys())

print(details.get('Name'))

print(details.get('Branch'))       # it return "None" as we don't have a "Branch" key

details.setdefault('Branch')      # As we don't have a key named as Branch, It Creates a key named as 'Branch'
print(details)

details.setdefault('Aname','Akash')        # we can create a key-value pair. But Cannot update value to existing key
print(details)


details.pop('Branch')              # we need to mention which key to pop
print(details.keys())

print(details.popitem())            # removes and return a key, value pair as a 2-Tuple
print(details)

del details['Id']
print(details.keys())

details.clear()              # removes all elements from dicktionary
print(details)



# fromkeys()

data = ['varun','sai','ram']

a = dict.fromkeys(data)           # Creates a dict but value set to None
print(a)
a['varun'] = 'hi'
print(a)

b = dict.fromkeys(['CGH1234','CGH2345'],['Code','gnan'])
print(b)


# TASK - Create a Dictionary with Personal details, similar to your Codegnan Profile



# Explanation of Dictionaries


















