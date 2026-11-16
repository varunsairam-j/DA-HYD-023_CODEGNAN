
# Sequences --> Strings, Lists, Tuples, Sets
# Mapping --> Dictionary

# Lists --> Collection of heterogeneous Elements
# List --> Indexed, Ordered, Mutable, Heterogeneous. We Use [] to store the Data
'''
Marks = [20,30,40,50]
print(Marks)
print(len(Marks))
print(type(Marks))
'''
# Operations: Indexing, Slicing, Striding, Membership, Merging, Repetition

# Nested Lists --> A list inside another list

'''
Names = ["Codegnan",25,4.6,[45,35,25,65],"DA23",34]

print(Names)
print(Names[0])
print(Names[3])

print(Names[0][:4])       # Output is Code
print(Names[0][4:])       # Output is gnan

# Get the Output as Cdga
print(Names[0][::2])

Names[0] = Names[0][::-1]
print(Names)

print(Names[3])
print(len(Names[3]))
print(Names[3][2])

'''
 
# Indexing, Slicing --> Mutable
'''
Names[2] = "Python"
print(Names)
'''

# By Indexing, If we change the elements, Length of Collection remains Same
'''
Names[5] = [1,2,3]
print(Names)
print(len(Names))

print(Names)
Names[2:5] = "Vsr","Jvsr"
print(Names)
'''
'''
Names = ['Codegnan',25,'Abhiram','Sai','Saketh','Sairam','DA23',23]
Names[3:6:2] = "Python","JAVA"
print(Names)
'''

# Create a nested List with Strings, Lists and work on Indexing, Slicing, Striding
# Added Advantage if i could add string functions in it

# List Functions --> append(), insert(), extend(), pop(), remove(), clear()

# index(), count(), copy(), sort(), reverse()

Names = ["Codeganan","Varun"]

# append() --> inserts single element to the end of the list

Names.append('Data')
#print(Names)

Names.append(["Data","Analytics"])

# append() will only add one element, will always increment the length of list by 1
'''
print(Names[3].append("ChatGPT"))       # It gives Output as None, as append is only applicable on list, not on print
'''
print(Names)

# extend() --> inserts multiple elements to the end of the list (should be given in a list)
'''
Names.extend("Analysis")      # String will be splitted
print(Names)

Names.extend(['Analysis'])
print(Names)

Names.extend(("Varun","Sai","Ram",30,7,2005))
print(Names)

Names = (1,2,3,"Varun")
print(Names)
'''

# insert() -->

Names.insert(1,"Python")
print(Names)

Names.insert(0,"Java")
print(Names)

# Names.insert([1:4]'['a','b'])    # Syntax Error

Names.insert(-1,"VSR")
print(Names)

# pop(), remove(), clear()

# pop() --> By Default Last. else, Given Index

print(Names.pop())
print(Names)

Names.pop(2)
print(Names)

# remove() --> we can remove a specific value

Names.remove("Data")
print(Names)

del Names[1:3]
print(Names)

Names.clear()  # Clear will remove all elements and returns empty list
print(Names)


# TASK --> Data = ['codegnan','saketh','python','java'] -- Input
# Output should be as follows
'''
    0 : codegnan
    1 : saketh
    2 : python
    3 : java
'''





























































































