#TASK - Guessing the Correct Number
'''
A = 0
Number = 123
while True:
    A = int(input("Guess the number: "))
    if Number == A:
        print("Your guess is correct")
        break
    elif A>123 and A<150:
        print("you are too close, Try Again by Decreasing the Number")
    elif A<123 and A>100:
        print("you are too close, Try Again by Increasing the Number")
    else:
        print("Wrong guess, Try Again")
'''
              
# TASK - Entering the Correct OTP
'''
Attempts = 1
OTP = 280506
while Attempts<8:
    Enter = int(input("Enter your OTP:"))
    if Enter == OTP:
        print("Authentication Success")
        break
    elif Attempts == 7:
        print("Maximum Attempts Reached, Try Again after 24 Hours")
        break
    else:
        Attempts += 1
        print("Try Again")
'''

# TASK - Counting Number of Items while Ordering Food
'''
Items = 0
while Items >= 0:
    Food = input("Enter the Food Item:")
    if Food != "EXIT":
        Items += 1
    else:
        print("No of Food Items Ordered:",Items)
        break
'''

        #or
'''
Food = input()
Count = 0
while Food != "EXIT":
    Count += 1
    Food = input()
print("Total No of Items Ordered",Count)
'''


  
   
        
        
        































    




































