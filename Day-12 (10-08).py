# Strings --> Caeconversions, Searching & Finding, String Testing methods, Replace, Space Removal

# Searching, Finding, Replacing

'''
A = "VarunSaiRam"

print(len(A))
print(min(A))
print(max(A))

B = A.index('S')     # Gives the Index Position of 'S' - 5
print(B)

C = A.index('a')     # Gives the First Occurence of 'a' - 1
print(C)

D = A.index('a',2)   # As we Already know the first occurence of 'a', We have to now when 'a' comes again
print(D)

E = A.index('a',10)   # Gives Value Error, as there is no 'a' after 10th Index
print(E)

F = A.index('x')    # Gives Error, as 'x' is not present in the given string
print(F)

G = A.index('a',2,5)    # Gives Error, as there is no 'a' in between 2nd and 5th Index
print(G)

'''

# rindex() --> Gives Last Occurence

'''
B = A.rindex('a')      # Gives the index position of 'a' from last - 9
print(B)

C = A.rindex('m')    # Gives index position of 'm' - 10
print(C)

D = A.rindex('m',11)     # Gives Error
print(D)

'''

# Count() --> returns the number of times the Object is repeating

'''
print('VarunSaiRam'.count('a'))

print(A.count('a'))

print(A.count('p'))     # As there is no 'p' in the string, It gives 0.

'''

# Find() --> Acts like index() but it avoids error & gives -1 if the substring is not found

'''
print(A.find('a'))    # Gives 1

print(A.find('e'))     # Gives -1, as 'e' is not present in the string, where index() gives error

print(A.rfind('a'))    # Gives last occurence

'''

'''
A = "DataAnalytics"
print(len(A))
for i in A:
    print(A.count(i),A.index(i))
'''

# Replacing, Splitting, Joining

#replace()
'''
A = "Codegnan"
A = A.replace('g','s')       # Replaces 'g' with 's' in the string
print(A)

print('Varun_Sai_Ram'.replace("_"," "))   # Removes "_"

'''

#split()
'''
A = 'Varun,Sai,Ram'
B = A.split(',')
print(B)

'''

#join()
'''
A = 'Code'
B = 'gnan'
print(A.join(B))
print(B.join(A))

print("#".join("Varun"))

'''

# String Testing Methods (Boolean)

# isalpha(), isalnum(), isdigit(), isupper(), islower()........

'''
A = "Codegnan123"
print(A.isalnum())      # Gives True if the string has Any of Alphabests or Numeric
print(A.isalpha())      # Gives True if string has only Alphabets
print(A.isdigit())      # Gives True if string has only Numbers   

B = "Codegnan"
print(B.isalpha())     
print(B.isalnum())
print(B.isdigit())

C = "123456789"
print(C.isdigit())
print(C.isnumeric())   # This has upper edge as it also includes Roman Numbers, Fraction along with Numbers

print("Varun".startswith('V'))          # Checks the starting of the String
print("VarunSaiRam".startswith('S',5))  # Can also check the middle of the string
print("Varun".endswith('s'))            # Checks the end of the String

print ("varun".islower())            # Returns True if all are lower case
print("VARUN".isupper())             # Return True if all are upper case
print("Varun Sai Ram".istitle())     # return True if every word starts with Upper Case

'''

# Space Removal --> strip() --> Removes Leading and Trailing spaces
'''
A = " VarunSaiRam "
print(A.strip())
B = input("Enter the String:").strip().lower().     # Here, it removes space and also converts all words into lowercase
print(B)

'''
'''
print("123".zfill(5))      # Fills Zeroes to the left of the number. Here, it will add 2 zeroes
print("123".zfill(8))      # Here, it adds 5 Zeroes

print("Hello".center(9))     # Gives spaces to left and right

print('Hello'.center(9,"@"))

print("Hai".ljust(6,"#"))     # Adjusts string to left and adds '#' in remaining spaces
print("Hai".rjust(6,"#"))     # Adjusts string to right and adds '#' in remaining spaces

'''












