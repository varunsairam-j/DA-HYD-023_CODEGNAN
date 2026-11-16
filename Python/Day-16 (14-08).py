# Sequences --> Strings, Lists, Tuples, Set, Frozen Set
# Mapping -->Dictionary

# Sets --> A Set is a Unique Collection of Elements (Objects) --> Unordered, Mutable
# Hashing, Unindexed, Unique, Heterogeneous

# set(), {}

# a = {} --> it is an empty dictionary
'''
a = set()
print(type(a))

student_ids = {123,345,234,564,234}
print(student_ids)
print(type(student_ids))
print(len(student_ids))

'''

# print(student_ids[2])          # Type Error

# print(student_ids*2)                  # Type Error --> Sets Cannot be Repeated
# print(student_ids + student_ids)      # Two Sets Cannot be Merged

'''
data = {12,3,4,5,[12,3,4],'saketh'}
print(data)                         # No Lists should be inside a Set (Hashing Technique), Lista are Mutable

'''
'''
data = {12,3,4,5,(12,3,4),'saketh'}
print(data)
print(len(data))
for i in data:
    print(i)

'''

# Methods on Sets --> add(), update(), remove(), discard(), pop()

#add()

'''
names = {'sai','saketh','kiran','codegnan'}
print(len(names))
names.add('python')
print(names)

names.add(('police','poll'))
print(names)

'''
#update()

da_names = {'mani','akash','sai','sonu'}
'''
names.update(da_names)
print(names)

'''
 
# remove(), discard(), pop(), clear()

# remove() removes an element from the set (it must be a member)
'''
da_names = {'mani','akash','sai','sonu'}

da_names.remove('sai')
print(da_names)
'''

# da_names.remove('sai')          # Key Error

# discard() will remove an element if its present in the set. else, it ignores
'''
da_names.discard('codegnan')
print(da_names)

'''
'''
da_names.pop()
print(da_names)
print(da_names.pop())       # removes and returns an Arbitary Element (Removes Element)
print(da_names)

da_names.clear()
print(da_names)

da_names.add('Sairam')
print(da_names)

da_names.update(['sai','akash'])
print(da_names)

'''

# copy()

d = da_names.copy()
print(d)

d.update({'python','codegnan'})
print(d)
print(da_names)


# Mathematical Opeartions --> union(), inttersection(), defference(), symmetric_difference()
# issubset(), issuperset(), isdisjoint()

# union()

da_23 = {12,23,34,45,23,36}
da_24 = {34,46,47,23}
da_25 = {1,2,3,4,45}

'''
event = da_23.union(da_24,da_25)     # we can also do this using symbols --> da_23 | da_24 | da_24
print(event)
print(len(event))

# intersection()

common = da_23.intersection(da_24)       # we can also do this using symbols --> da_23 & da_24
print(common)
print(len(common))

common = da_23.intersection_update(da_24)       # Updates the Intersection Elements to da__23
print(common)
print(da_23)

'''
'''
print(da_23)
print(da_24)

# difference() --> removes common elements and prints remaining elements from first set

diff = da_23.difference(da_24)
print(diff)

      #or

f = da_23 - da_24
print(f)

symm = da_23.symmetric_difference(da_24)
print(symm)

       #or

s = da_23 ^ da_24
print(s)


# issubset() --> checks for all elements to be present in other set

da_24.remove(46)
da_24.remove(47)

print(da_24.issubset(da_23))
print(da_23.issuperset(da_24))

# isdisjoint() --> return False for sets having common elements

print(da_23.isdisjoint(da_24))

'''

# Length of Unique student ids in a class, where user can  enter first input
# He should be giving number of student_ids, He will enter student_ids

n = int(input("Enter No.of Ids: "))
student_ids = input("Enter Student Ids: ").split()

# print(student_ids)

result = set(student_ids)
print(result)
print(len(result))















