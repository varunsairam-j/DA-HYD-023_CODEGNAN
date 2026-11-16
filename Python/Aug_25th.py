# super().__init__()   # Calls Super class Constructor
# super().__init__(args)    # calling super class Constructor with arguments
# super().method()

'''
class Father:
    """Usage of Constructor in Single Inheritance"""
    def __init__(self,property):
        self.property = property
    def father_property(self):
        print(f'Father Property is {self.property}')
class Kid(Father):
    """Now Child class will have constructor"""
    def __init__(self,cash,property):
        self.cash = cash
        super().__init__(property)        # Calls super class Constructor with arguments
    def kid_property(self):
        print("Kid Property is",self.cash)
        print("Total Property is",self.property + self.cash)

obj = Kid(250000,1000000)
obj.kid_property()
obj.father_property()

'''

# What if Child Class is having same method name as Parent Class
# Method Overriding 

# Finding out Area of Squares / Rectangles
'''
class Rectangle:
    """Method Overriding Usage"""
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def r_area(self):
        print(f"Area of Rectangle is {self.x * self.y}")
class Square(Rectangle):
    def __init__(self,x):
        self.x = x
    def area(self):
        print(f"Are of Square is {self.x ** 2}")

obj = Square(10)
obj.area()
# obj.r_area()    # Raises Error

'''

# We will make Rectangle aS Child Class

'''
class Square:
    """Method Overriding Usage"""
    def __init__(self,x):
        self.x = x
    def area(self):
        print(f"Area of Square {self.x ** 2}")
class Rectangle(Square):
    def __init__(self,x,y):
        self.y = y
        super().__init__(x)
    def area(self):
        super().area()          # Calling Super class Method
        print(f"Area of Rectangle is {self.x * self.y}")

x,y = map(int,input("Enter the Values of x and y:").split(','))
obj = Rectangle(x,y)
obj.area()

'''

# Syntax --> Multiple Inheritance

'''
class Parent 1:
    .........
class Parent 2:
    .........
class Child(Parent 1,Parent 2):
    .........
'''
# Example -->

'''
class User:
    """First parent class with user feathures"""
    def voice_call(self):
        print('Making Voice Calls')
class Notifications:
    def notifications(self):
        print("Sending Notifications...")
class Premium_User(User,Notifications):
    def verification_badge(self):
        print("Blue Tick Verification done")

obj = Premium_User()
obj.voice_call()
obj.notifications()
obj.verification_badge()

'''

# Syntax --> Multilevel Inheritance

'''
class Grand Parent:
    .........
class Parent (Grand Parent):
    .........
class Child(Parent):
    .........
'''
# Example -->

'''
class User:
    """Grand Parent Class"""
    def video_call(self):
        print('Making Video Calls')
class Business_User(User):
    def catalog(self):
        print("Catalog Features Available")
class Verified_User(Business_User):
    def verification_badge(self):
        print("Blue Tick Verification done")

obj = Verified_User()
obj.video_call()
obj.catalog()
obj.verification_badge()

obj_1 = Business_User()
obj_1.verification_badge()

'''

# Syntax --> Hierarchical Inheritance

'''
class Parent:
    .........
class Child_1(Parent):
    .........
class Child_2(Parent):
    .........
class Child_3(Parent):
    .........
'''
# Example -->

'''
class Player():
    """Hierarchical Inheritance Use"""
    def Stats(self):
        print("Player Stats are:______")
class Batting(Player):
    def Batter(self):
        print("Player Batting Stats are:_____")
class Bowling(Player):
    def Bowler(self):
        print("Player Bowling stats are:_____")
class All_Round(Player):
    def All_Rounder(self):
        print("Player's Batting & Bowling Stats are:_____")

obj = All_Round()
obj.Stats()
obj.All_Rounder()

'''

# Syntax --> Hybrid Inheritance 

'''
class A:
    .........
class B(A):
    .........
class C(A):
    .........
class D(B, C):
    .........
'''
# Example -->

class Free_Fire():
    def Games(self):
        print("Can Play Games")
class Prime_Level_1(Free_Fire):
    def L_1(self):
        print("Obtain Prime-1 Symbol, Avatar & Banner")
class Prime_Level_2(Free_Fire):
    def L_2(self):
        print("Obtain Gloo wall skin & Extra Outfit Slot")
class Next_Levels(Prime_Level_1, Prime_Level_2):
    def N_L(self):
        print("Obtain Emote,Extra Friend Slots & Prime Invite,Profile")
class Prime_Level_8(Next_Levels):
    def L_8(self):
        print("Obtain Prime Store, Outfit Sharing & Prime Badge")

obj = Prime_Level_8()
obj.Games()
obj.L_1()
obj.L_2()
obj.N_L()
obj.L_8()


# Inheritance, Super Method


