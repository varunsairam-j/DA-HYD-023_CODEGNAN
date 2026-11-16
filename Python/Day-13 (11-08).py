# TASK-1 -->

# ''' Program by Google Gemini '''
'''
# Step 1: Get input from the user
user_input = input("Enter a sentence: ")

# Step 2: Describe the original text using conditional checks
print("\n--- Original Text Description ---")
if user_input.isupper():
    print("The original text is entirely in UPPERCASE.")
elif user_input.islower():
    print("The original text is entirely in lowercase.")
elif user_input.istitle():
    print("The original text is in Title Case.")
else:
    print("The original text is in a mixed or uncategorized case.")

# Step 3: Store case-conversion method names in a collection (list of strings)
# We map the descriptive label to the actual string method name
cases = ["upper", "lower", "title", "capitalize", "swapcase"]

print("\n--- Case Conversions ---")
# Step 4: Use a loop to dynamically call each method and display the result
for case in cases:
    # getattr() allows us to call a method on the string object by its string name
    converted_text = getattr(user_input, case)()
    
    # Format the label for clean alignment (e.g., 'upper' -> 'Upper')
    label = case.capitalize() if case != "swapcase" else "Swap case"
    print(f"{label:<13}: {converted_text}")
'''

# ''' Program by me ''' ( Doesn't Satisfy Requirements )

'''
String = input("Enter a Sentance:")

print("Upper: ",String.upper())
print("Lower: ",String.lower())
print("Title: ",String.title())
print("Capitalize: ",String.capitalize())
print("Swapcase: ",String.swapcase())

'''

'''
user_input = input("Enter a sentence: ")
cases = ["upper", "lower", "title", "capitalize","swapcase","isupper"]
for case in cases:
    print(getattr(user_input, case)())
'''


# TASK-2 -->

'''
Username = input("Enter a Username:")
while Username != "Quit":
    if Username.isalnum():
        print("Contains Only Letters and Numbers")
    else:
        print("Does not Contains Only Letters and Numbers")
    if Username.isidentifier():
        print("Begins with a Letter")
    else:
        print("Not a Valid Identifier")
    if Username.isascii():
        print("Contains Only ASCII Characters")
    else:
        print("Does not Contains Only ASCII Characters")
    if Username.isalpha():
        print("Contains only Letters")
    else:
        print("Does Not Contains only Letters")
    Username = input("Enter a Username:")
while Username == "Quit":
    print("Ended")
    break
'''       
        
        
        




















