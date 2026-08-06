'''
Control Statements --> Control of Flow of Execution of Program
--> Conditional Statements --> if,elif,else...

--> Repetition Statements (Loops) --> for,while (for with else, while with else...)
--> Jumping Statements --> break,continue,pass
'''

# Loops --> Loops are helpful for repetition (Automative tasks)
# for keyword will be helpful to iterate over a sequence / range

# Syntax for (for keyword):
'''
for <temp_var> in sequence/range:
    statement(s)...
    ......
'''
# range(start,stop,step)
# By Default, range picks 0 as start value
'''
for i in range(10):
    print(i)
'''
# In Above case, we got 10 iterations
'''
for i in range(1,10):
    print(f"The Value of i is {i}")
'''
'''
for i in range(1,10):
    if i>5:                               # if we want to keep another condition like to print only even, we can add ( and i%2==0 )
        print(f"The Value of i is {i}")
'''

# range(start,stop,step)  --> here step --> interval
'''
for i in range(1,10,2):     # The 3rd Number indicates the Gap between Numbers
    print(i)            # Output is 1,3,5,7,9
    print("Done")
'''
'''
for i in range(10,1,-1):     # For Counting the Numbers in Reverse Order
    print(i)            # Output is 10,9,8,7,6,5,4,3,2
'''
'''
for i in range(10,-10,-2):     # Also counts Negative Numbers
    print(i)            # Output is 10,8,6,4,2,0,-2,-4,-6,-8
'''

# [] --> Lists
'''
names = ['Varun','Sai','Ram']
for name in names:
    print(name)
'''
'''
names = ['Varun','Sai','Ram']
print(len(names))             # len(obj) --> return the number of items in a container. Output is 3 
for name in names:
    print(name)
    print(f"Student Name is {name}")
    if name == "Sai":
        print(f"Student Name is {name}")
'''
    
# Caluculate the Sum of first 10 Numbers

# First, Understand our input. range(11) --> 10 Numbers
# Second, Understand our Output --> sum (number)
# Third, we need to map the logic
'''
for i in range(11):
    print(i)
    print(f"Result is {i+i}")    # This doesn't give the output
'''

# Caluculate the Sum of first 10 Numbers
'''
result = 0
for i in range(11):
    result = result + i
    print(f"Now the result is {result}")
print(f"Sum of 10 Numbers is {result}")
'''

# Caluculate the Sum of first 10 Even Numbers ( changing the range)
'''
result = 0
for i in range(0,21,2):
    result = result + i
    print(f"Now the result is {result}")
print(f"Sum of 10 Numbers is {result}")
'''
# Caluculate the Sum of first 10 Even Numbers (By using Condition)
'''
result = 0
for i in range(21):
    if i%2==0:
        result = result + i    #result += i 
print(result)
'''

# Understand the loops usage with Fitness streak Example
# Work_Out --> 1 , work_out_missed --> 0
<<<<<<< HEAD:Day-6 (03-08) .py
=======

>>>>>>> 6d653915dee7bbb518aa50eb92046e224c4aa8b1:Day-6.py
'''
work_log = [0,1,1,1,0,1,0,1]
#result variable --> longest_streak
longest_streak = 0
current_streak = 0
for day in work_log:
    if day == 1:
        current_streak = current_streak + 1
        if current_streak > longest_streak:
            longest_streak = current_streak
    else:
        current_streak = 0                       #streak breaks
print(f"longest_streak is {longest_streak}")
<<<<<<< HEAD:Day-6 (03-08) .py
'''
=======
'''        
  




>>>>>>> 6d653915dee7bbb518aa50eb92046e224c4aa8b1:Day-6.py








