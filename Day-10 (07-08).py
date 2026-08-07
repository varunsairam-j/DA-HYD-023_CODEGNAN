# TASK - Caluculating the Innings of a Batsman
'''
Balls = Total_Runs = Dot_Balls = Boundaries = 0
List = [0,2,4,1,0,2,4,6,2,3,1,0,0,2,4,6,6,2,0,1,3,2,4]
for i in List:
    Balls += 1
    Total_Runs += i
    if i == 0:
        Dot_Balls += 1
    if i == 4 or i == 6:
        Boundaries += 1
print("Balls Faced:",Balls)
print("Runs Scored:",Total_Runs)
print("Dot Balls:",Dot_Balls)
print("Boundaries:",Boundaries)
    
'''  
    
# TASK - Locking the Phone if the Password is wrong
'''
Attempts = 0
Password = 300705
while Attempts<5:
    Enter = int(input("Enter Your Password:"))
    if Enter == Password:
        print("Phone Unlocked")
        break
    else:
        Attempts += 1
        print("Try Again")
'''    

    
























