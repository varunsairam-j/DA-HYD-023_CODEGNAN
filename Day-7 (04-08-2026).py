#Usage of else with for --> the else keyword will only be executed when the loop is completely done without any break

# for with else...
'''
work_log = [0,1,1,1,0,1,0,1]
longest_streak = 0
current_streak = 0
for day in work_log:
    if day == 1:
        current_streak = current_streak + 1
        if current_streak > longest_streak:
            longest_streak = current_streak
            print(longest_streak)
    else:
        current_streak = 0                       #streak breaks
else:
    print(f"longest_streak is {longest_streak}")     # In this case, when the loop execution is done, we get result of else block
'''

# Same Program with break usage
'''
work_log = [0,1,1,1,0,1,0,1]
longest_streak = 0
current_streak = 0
for day in work_log:
    if day == 1:
        current_streak = current_streak + 1
        if current_streak > longest_streak:
            longest_streak = current_streak
            print(longest_streak)
            break
    else:
        current_streak = 0                       #streak breaks
else:
    print(f"longest_streak is {longest_streak}")     # In this case, when the loop execution is done, we get result of else block
print("Execution Done")
'''

# for-else with Notification Scenario
'''
notifications = [0,0,0,0]
for notification in notifications:
    if notification == 1:
        print("Unread Notifications")
        break
else:
    print("All Caught Up")
'''
# Try to take notifications from user
'''
notifications = list(map(int,input("Enter the Values --> 0 or 1:").split(',')))
print(notifications)
for notification in notifications:
    if notification == 1:
        print("Unread Notifications")
        break
else:
    print("All Caught Up")
'''

# while --> it relies on condition, it will be completely executed until the condition is satisfied
'''
syntax of while:

while <condition>:
    statement(s).....
    .....
    .....
'''

'''
while True:
    print("Yes")  # The Loop doesn't end. So, The Output displays Yes infinitely. To Interrupt, Ctrl+C (Keyboard Interrupt)
'''

# Print Numbers from 0 to 10

'''
i = 0           # Initialised Statement
while i<=10:
    print(i)
    i = i+1     # Counter
''' 

# Print Numbers from 10 to 0
'''
i = 0           
while i<=10:
    print(10-i)
    i = i+1
'''
    
# Banking Scenario --> PIN Authentication, if more than 3 attempts --> Account Locked

pin ="3007"
max_attempts = 3
current_attempt = 0
while current_attempt < max_attempts:
    entered_pin = input('Enter your ATM Pin:')
    if entered_pin == "3007":
        print("Login Successful")
        break
    else:
        print("Entered Pin is Wrong...Try Again Carefully")
         current_attempt = current_attempt + 1
else:
    print("Max Attempts Reached, Try again Tomorrow")
    












    











