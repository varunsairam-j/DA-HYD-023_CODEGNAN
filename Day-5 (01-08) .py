# Method that Sir said by using if & else -
'''
Marks = int(input("Enter Your Marks (1-100):"))
if Marks>0 and Marks<=100:
    if Marks>=90:
        print("You have secured 'A' Grade")
    if Marks>=80 and Marks<90:
        print("You have secured 'B' Grade")
    if Marks>=70 and Marks<80:
        print("You have secured 'C' Grade")
    if Marks>=60 and Marks<70:
        print("You have secured 'D' Grade")
    if Marks<60:
        print("You have Failed in the Exam, Study Again")
else:
    print("Enter only +ve Values greater than 0 and less than 100")
'''

# Method that Sir said by using elif -
'''
Marks = int(input("Enter the Student Marks:"))
if Marks>=100:
    print("Entered Values should be greater than 1 and less than 100")
elif Marks>=90 and Marks<=100:
        print("User have secured 'A' Grade")
    if Marks>=80 and Marks<=89:
        print("User have secured 'B' Grade")
    if Marks>=70 and Marks<=79:
        print("User have secured 'C' Grade")
    if Marks>=60 and Marks<=69:
        print("User have secured 'D' Grade")
    if Marks<60 and Marks>=0:
        print("User have Failed in the Exam,Study again")
else:
    print("No Negative values")
'''

# TASK - Try Same Usecase with if-elif-else in other way


# Voter Eligibility Checkcase --> Make sure to satisfy all possible conditions
# >=18 and 100 --> Access
# <18 --> No. Of Years Eligibility should tell
# Negative Vaalues --> Not Acceptible
'''
age = int(input("Enter the age:"))
if age>=18 and age<=100:
    print("-----User has Vote Eligibility-----")
    print("-----Access Granted-----")
elif age<18 and age>0:
    print("-----User still need to get vote eligibility-----")
    print("-----User still need to wait for",(18-age),"year(s)-----")
else:
    print("-----Only +ve Values and less than 100 Acceptable-----")

# Prefer if-elif-else
'''

# Output Formatting --> Old Style formatting (using commas)
# Percentile (%) usage (%f,%d) , .format() usage , fstring notation
'''
a,b = 10,20
print(a)
print(b)   # Normal Output Format
print(a,b)  # Output using Commas

name = 'Varun'; place = 'Ongole'
print(name,place)  # By Default, sep is having space
print(name,place,sep=',')

# end='\n' , \t --> Tab Space

print(name,place,end='\n')   # By using end='\t', The Next Print will be displayed in this same line in the output by having Tab Space
print(a,b,end=',')  # If we leave (end='') like this, will be displayed withoput tab space
print("Ongole")

Name = 'Varun'; Age ='21';Place = 'Ongole'; Course = 'DA'
#Usage of Commas
print('my name is',Name,'of age',Age,'is in',Place,'studying',Course)
'''

#Old Style Formatting --> %d --> Integer , %s --> string , %f --> float
'''
salary = 25000
print("His salary is %d"%(salary))
print("His salary is %f"%(salary))
print("His salary is %.1f"%(salary))  # Rounding to 1 decimal
'''

# .format() usage
'''
name = 'Varun'
place = 'England'
print("{} is in {}".format(name,place))  # Order matter
'''
# f string method
'''
print(f'{name} is in {place}')   
print(f'{"Saketh"} is in {name}')
'''























