# Grade Checker (Grade and Remarks)

Marks = int(input("Enter your Marks:"))
if Marks>0 and Marks<=100:
    if Marks>=90:
        print("Grade-A")
        print("Remark: Outstanding!")
    elif Marks>=80:
        print("Grade-B")
        print("Remark: Excellent!")
    elif Marks>=70:
        print("Grade-C")
        print("Remark: Good")
    elif Marks>=60:
        print("Grade-D")
        print("Remark: Fair, needs improvement")
    elif Marks>=50:
        print("Grade-E")
        print("Remark: Poor, needs serious improvement")
    else:
        print("Grade-F")
        print("Remark: Failed, needs to reappear")
else:
    print("Invalid Marks Entered")



# Even - Odd Checker (with a Twist)

A = int(input("Enter a Number:"))
if A%2==0:
    if A>0:
        print("Even Number")
    elif A<0:
        print("Negative Even Number")
    else:
        print("Zero is Neither Even nor Odd")
elif A%2!=0:
    if A>0:
        print("Odd Number")
    elif A<0:
        print("Negative Odd Number")
    else:
        print("Zero is Neither Even nor Odd")



# Season Identifier 

A = int(input("Enter Month Number:"))
if A>0 and A<=12:
    if A==1 or A==2 or A==12:
        print("Season: Winter")
    elif A==3 or A==4 or A==5:
        print("Season: Spring")
    elif A==6 or A==7 or A==8:
        print("Season: Summer")
    elif A==9 or A==10 or A==11:
        print("Season: Autumn")
else:
    print("Invalid Month Entered")


#--------------------------------------------------------------- TASK COMPLETEED --------------------------------------------------------------------------#
    




















    
