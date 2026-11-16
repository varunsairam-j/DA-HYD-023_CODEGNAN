# Polymorphism

'''
Polymorphism --> It is also one of the Key Feature of OOP
Poly --> Many 
Morph --> Forms
--> Methods with Same Names can take different parameters (arguments)

--> Method Overloading ( Compile time polymorphism )
--> Method Overriding ( Run-Time )
--> Operator Overloading (+,*) (__add__,__str__)

'''

# Example --> Hotstar

'''
--> Free User --> Can watch some Movies with Advertisements
--> Premium User --> Can watch Premium Content (More Movies & Series) without Advertisements
--> VIP User --> Live Content, Streaming Quality, Premium Quality without Advertisements

'''

# Method Overloading :

'''
class Hotstar:
    """Understanding Polymorphism"""
    def watch():
        print(f"User Logged into Hotstar...... Opening Home Page")
    def watch(self,movie):
        self.movie = movie
        print(f"User is Watching {self.movie} Movie")

app = Hotstar()
app.watch("The Dark Knight")
# app.watch()   -->  It returns error as watch() is Overloaded

'''

# 1) Method Usage with Default Arguments
# 2) Method Usage with Variable Length Arguments (*args)
# 3) Method Usage with Type of Arguments

# 1) Method Usage with Default Arguments
'''
class Hotstar:
    """Method Usage with Default Arguments"""
    def watch(self,movie=None):
        if movie is None:
            print(f"User Logged into Hotstar....Checking for New Movies")
        else:
            self.movie = movie
            print(f"User Started watching {self.movie} Movie")

app = Hotstar()
app.watch()
app.watch("Vikram")
'''

# 2) Method Usage with Variable Length Arguments (*args)

'''
class Hotstar:
    def watch_list(self,*movies):
        if len(movies)==0:
            print("User did not add any Movies to Watch list")
        else:
            for i in movies:
                self.movies = movies
                print(f"User added the {i} movie in watch list")

user = Hotstar()
user.watch_list()
user.watch_list("The Batman Begins","The Dark Knight","The Dark Knight Rises")

'''
#                                    or
'''
class Hotstar:
    def watch_list(self,*movies):
        print(movies)
        for movie in movies:
                self.movie = movie
                print(f"User added the {movie} movie in watch list")

user = Hotstar()
user.watch_list()
user.watch_list("The Batman Begins","The Dark Knight","The Dark Knight Rises")
                        
'''

# 3) Method Usage with Type of Arguments

# Example --> One Movie at a time or Can watch Multiple Movies ( Start watching one Movie, go back, start another)

'''
class Hotstar:
    """Method Overloading with Type of arguments Usage"""
    def watch(self,content):
        if isinstance(content,str):
            print(f"User Watching {content}")
        elif isinstance(content,list):
            print("Your Playlist:")
            for movie in content:
                print(movie)

user = Hotstar()
user.watch("Game of Thrones")

user_2 = Hotstar()
user_2.watch(["House of the Dragon","The Knight of Seven Kingdoms","Aegon's Conquest"]) 

'''

# Method Overriding --> It Happens in the scenario of Inheritance, where id child class is having same method name as parent class
# So, we use super() or if we create different objects
'''
class Free_User:
    """Understanding Method Overriding"""
    def watch(self):
        print("User logged into Homepage....")
class Premium_User(Free_User):
    """Using Inheritance"""
    def watch(self,movie):
        self.movie = movie
        print(f"User watching {self.movie}")

obj = Premium_User()
obj.watch("RRR")

obj_2 = Free_User()
obj_2.watch()

'''
# In above case, we can create different 

'''
class Free_User:
    """Understanding Method Overriding"""
    def watch(self):
        print("User logged into Homepage....")
class Premium_User(Free_User):
    """Using Inheritance"""
    def watch(self,movie):
        super().watch()      # Calling Superclass Method
        self.movie = movie
        print(f"User watching {self.movie}")

obj = Premium_User()
obj.watch("Avengers")

'''

# Operator Overloading --> Operators (+,-,*,/) --> Opearots will behave in a different way as per user defined functions

# + ( Addition,Concatenation,Merging)

'''
print(3 + 4)               # Addition
print('code' + 'gnan')     # Concatenation
print([23,45] + [91,97])   # Merging 

# print(3.__add__(4))      # __add__(self,other)

a = 25 ; b = 35            # Addition
print(a.__add__(b))

a = [1,2,3] ; b = [4,5,6]  
print(a.__add__(b))    # Merging
print(a.__len__())     # len(a)
print(a.__mul__(2))    

'''

# Let's apply the above scenario to Hotstar Watch History

'''
class Watch_History:
    """Define the Number of Watch Hours"""
    def __init__(self,Hours):
        self.Hours = Hours

varun = Watch_History(100)
print(varun.Hours)

akash = Watch_History(120)
print(akash.Hours)

# print(varun + akash)            # Type Error, Unsupported Operation
print(varun.Hours + akash.Hours)

'''

# But, The Preferable way is usage of __add__()

'''
class Watch_History:
    """Define the Number of Watch Hours"""
    def __init__(self,Hours):
        self.Hours = Hours
    def __add__(self,other):
        return self.Hours + other.Hours
    def __str__(self):
        return f'{self} Watch History is {self.Hours}'

varun = Watch_History(300)
print(varun)    # __str__() Method
print(varun.Hours)
akash = Watch_History(100)
print(akash)
print(akash.Hours)

'''

















