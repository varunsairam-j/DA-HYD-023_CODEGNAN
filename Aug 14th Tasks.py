
# Question 1: Student Marks Manager

'''
Marks = []
while len(Marks)<3:
    marks = int(input("Enter the Marks: "))
    Marks.append(marks)

print("Marks Entered by User:",Marks)

Marks.insert(0,90)

Marks.extend([75,85])

print("Updated Marks List:",Marks)

if 75 in Marks:
    Marks.remove(75)

print("Removed Marks:",75,'and',Marks.pop())

print("Final Marks List:",Marks)
print("No.of Marks in the List:",len(Marks))

'''


# Question 2: Number List Analyser

'''
List = [20, 10, 30, 20, 40, 20]

List.sort()
print("Ascending Order of the List:",List)
for number in List:
    print(number, end=" ")
 
List.reverse()
print("\nDescending Order of the List:",List)
for number in List:
    print(number, end=" ")

Number = int(input("\nEnter a Number:"))

if Number in List:
    print("Entered Number is present in the List")
    print("The Entered Number is Repeating",List.count(Number),"times")
    print("The Entered Number's first index is",List.index(Number))
else:
    print("Entered Number is not present in the List")

print("Minimum Number in the List is",min(List))
print("Maximum Number in the List is",max(List))
print("The Sum of the Numbers in the List is",sum(List))
    
'''


# Question 3: Even and Odd Number Separator

'''

List = [10, 15, 20, 25, 30, 35]

Even = []
Odd = []

for number in List:
    if number%2==0:
        Even.append(number)
    else:
        Odd.append(number)
        
print("First Three Numbers in the List:",List[0:3])
print("Last Three Numbers in the List:",List[-3:])

print("Even Number List:",Even)
print("Odd Number List:",Odd)

Copied_List = List.copy()

List.clear()

print("Original List:",List)
print("Copied List:",Copied_List)

'''


# Question 4: Unique Name Manager

'''
Names = ["Asha", "Rahul", "Asha", "John", "Rahul"]

Names = set(Names)

Names.add("Meera")

Names.update(["Arun","Priya"])

if 'John' in Names:
    Names.remove('John')

Names.discard('David')

for names in Names:
    print(names)

'''


# Question 5: Course Student Comparison

'''
python_students = {"Asha", "Rahul", "John", "Meera"} 
da_students = {"Rahul", "Meera", "Arun"} 

print("All Students from both courses:")
Union = python_students | da_students
for students in Union:
    print(students)

print("Students learning both courses:")  
Intersection = python_students & da_students
for students in Intersection:
    print(students)

print("Students learning only Python:")    
Difference = python_students - da_students
for students in Difference:
    print(students)

print("Students learning only any one course:")    
Symmetric = python_students ^ da_students
for students in Symmetric:
    print(students)

if da_students.issubset(python_students) and python_students.issuperset(da_students):
    print("da_students is Subset of python_students - True")
    print("python_students is Superset of da_students - True")
else:
    print("da_students is Subset of python_students - False")
    print("python_students is Superset of da_students - False")
if python_students.isdisjoint(da_students):
    print("python_students and da_students are both dis-jointsets - True")
else:
    print("python_students and da_students are both dis-jointsets - False")

'''









