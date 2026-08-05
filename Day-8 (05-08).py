# Sequences --> Strings, Lists, Sets, Tuples, Mapping (Dict)

# Strings --> Group of characteres --> we use single or double or triple quotes for representation of strings
# Strings are Immutable, Ordered, Indexed Collection
'''
name = "Varun"
print(name)
print(type(name))
print(len(name))     # len --> returns the number of items in a container
'''
# Index --> Used to fetch the object (Position). It Always start at 0 & Ends at len(obj)-1
# We use [] representation
'''
print(name[0])
print(name[25])      # Index Error --> Out of Range
'''
# Negative Indexing --> -1 to -len(obj)
'''print(name[-1])'''

# Slicing of String --> We can access group of characters (objects)
# we use [start:end]   # Start Default --> 0. Start is Excluded, End is Excluded.
'''
name = "Varun"
print(name)
print(name[:])    # Return entire string
print(name[2:4])       # starts at "r"- 2nd Index(3) and Ends at before 4th Index "u" - 3rd Index(4)
print(name[0:50])   # Returns till the end of the String
'''

'''print(name[4:1])'''   # Return Empty String. Because, Strings are Immutable
# Slicing is Applicable from Lower Index to Higher Index.
'''
name = "Varun"
print(name)
print(name[-1:-5])   # returns empty string because it doesn't print from back to front
print(name[-5:-1])    # prints "Varu"
'''
# Print "aru" from the name using both positive and negative index

'''print(name[1:4])
print(name[-4:])'''       # We should leave the end position

# Observe all the possibilities --> +ve,+ve -ve,-ve +ve,-ve

# Striding --> [start:end:step]
'''
place = "Hyderabad"
print(len(place))
print(place[:3])
print(place[-3:])

print(place[::1])   # Returns all characters
print(place[::2])   # Prints by skipping 1 letter in between letters
'''
'''
course = "DataAnalysis"
# To Print tnys
print(course[2::3])

print(course[::-1])
print(course[::-2])
'''

# TASK --> Workout with all possibilities of slicing and striding on a example

'''name = "Varun"'''
# name[3] = "w"    # We cannot assign like this

# Operations on Strings --> Indexing, Concatenation, Repetition, Membership

'''print(name * 3)
print("_" * 10)'''    # Repetition

# Concatenantion --> Combining Strings

'''name = "Varun"+" "+"Sai"+" "+"Ram"
print(name)'''

'''
print("Varun" in "VarunSaiRam")     # Prints True

for name in "Varun":
    print(name)           # We get Every Character line by line

for name in "Varun":
    print(name,end=",")
'''

'''name = "Codegnan"'''

# Built-in Functions  --> len(),min(), max(),sorted()
'''
print(len(name))
print(min(name))     # Alphabetical Order as per ASCI Values
print(ord("A"))     # ord() gives the ASCI Values of the character
print(ord("a"))     
print(chr(122))     # chr() gives the character for the ASCI Number
print(max(name))

print(sorted(name))   # prints ['C', 'a', 'd', 'e', 'g', 'n', 'n', 'o'] - by sorting out the elements
'''

# Methods on Strings --> Case-Conversions, Finding/Searching

# Case Conversions ---> upper() lower() title() capitalize()

name = "Varun's Codegnan"
a = name.upper()            # Makes every letter Capital
print(a)     

b = name.lower()            # Makes every letter Lower
print(b)                   

c = name.capitalize()       # Makes first letter Capital and every other letter small
print(c)

d = name.title()            # Makes Every Word (first letter after the space) to Capital Letter 
print(d)  


# TASK - A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# Use Loops and Strings to return A-Z














































































