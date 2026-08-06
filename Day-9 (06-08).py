# TASK -1  - To Caluculate the Cost of All Products in the Cart
'''
Sum = 0
Cost = list(map(int,input("Cost of the Products in the Cart:").split()))
print(Cost)
for i in range(len(Cost)):
    Sum = Sum + Cost[i]
print(Sum)

'''
      #or
'''
for i in Cost:
    Sum+= i
print(Sum)

'''


# TASK -2 - Password Analyzer
'''
U = 0
L = 0
S = 0
N = 0
Password = input("Enter Your Password: ")
for i in Password:
    if i>=chr(65) and i<chr(91):
        U = U + 1
    if i>=chr(97) and i<chr(123):
        L = L + 1
    if (i>=chr(33) and i<chr(48)) or (i>=chr(58) and i<chr(65)) or (i>=chr(91) and i<chr(97)) or (i>=chr(123) and i<=chr(126)):
        S = S + 1
    if (i>=chr(47) and i<chr(57)):
        N = N + 1
print(f"Total Capital Letters:{U}")
print(f"Total Small Letters:{L}")
print(f"Total Special Characters:{S}")
print(f"Total Digits:{N}")

'''
        #or
'''
password = input()
upper=lower=digit=special= 0
for ch in password:
    if 'A'<=ch<='Z':
        upper += 1
    elif 'a'<=ch<='z':
        lower += 1
    elif '0'<=ch<='9':
        digit += 1
    else:
        special += 1
print("Upper Letters:",upper)
print("Lower Letters:",lower)
print("Digits:",digit)
print("Special Characters:",special)

'''

# TASK - Domain Collector

'''
email = input().split()
for mail in email:
    print(mail.split("@")[1])
'''

# TASK - Movie Watchlist in a Line










































