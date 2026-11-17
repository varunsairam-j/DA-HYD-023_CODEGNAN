'''
OOP --> Class, Object, Method (__init__)
Encapsulation --> Public, Protected, Private
'''

# Inheritance --> It is one of key feature of OOP where we inherit the properties (Attributes/methods) from one class to another
# Base Class (Parent Class) --> Derived Class (Child Class)
# Features --> Code Reusability, Avoiding Code  Duplication, Code Maintainability, 
# Polymorphism ( Method Overriding (super()), Overloading, Operator Overriding (__add__,__str__))

'''
Types : 

# Single Inheritance (Fingerprint) 
--> One Child class inheriting properties from one parent class

# Multiple Inheritance (Mother,Father --> Child) --> One Child
--> Class Inheriting Propertiess from two parent classes

# Multilevel Inheritance (Grand Parent --> Parent --> Child)
--> Level by Level

# Hierarchical Inheritance --> Multiple Child Classes
--> Inheriting properties from single parent class

# Hybrid Inheritance --> It can carry one or more type of imheritances

'''

# Syntax ( Single Inheritance ) :
'''
class baseclass:
    statements(s)..
    .......
class Derivedclass(baseclass):
    ........
    ......
'''
# Whatsapp Scenario --> Personal User, Business User
'''
class User:
    """Single Inheritance usage"""
    def send_message(self):
        print('Sending Messsage')
    def voice_call(self):
        print('Making Voice Calls')
    def video_call(self):
        print('Making Video Calls')
class Business_User(User):
    #pass
    def create_catalog(self):
        print("Displaying Produts Catalog")

U1 = Business_User()
print(dir(U1))
U1.send_message()
U1.video_call()
U1.voice_call()
U1.create_catalog()

'''

# Social Media Login --> Users --> update_users
'''
class Users:
    """Single Inheritance Usage"""
    company = "Codegnan"        # class attribute
    def __init__(self,f_name,l_name):
        self.f_name = f_name
        self.l_name = l_name
    def full_name(self):
        return self.f_name + self.l_name

# U1 = Users("VarunSaiRam","Joolapalli")
# print(U1.full_name())
# print(U1.company)

class Update_Users(Users):
    def update_name(self):
        return self.f_name.title()+" "+self.l_name.title().strip()

U1 = Update_Users("VarunSaiRam","Joolapalli")
print(U1.company)
print(U1.full_name())
print(U1.update_name())        

U2 = Users("Sai","Vemula")
print(U2.full_name())
print(U2.company)

'''

# what if we have constructor in child class also...
# Father --> Kid (Property)

'''
class Father:
    """Usage of Constructor in Single Inheritance"""
    def __init__(self):
        self.property = 1000000
    def father_property(self):
        print(f'Father Property is {self.property}')
class Kid(Father):
    """Now Child class will have constructor"""
    def __init__(self):
        super().__init__()         # Calling Superclass Constructor
        #self.property = 200000
        self.cash = 200000
    def kid_property(self):
        print("Kid Property is",self.cash)
    def total_property(self):
        print("Total Property is",self.property + self.cash)

obj = Kid()
obj.father_property()
obj.kid_property()
obj.total_property()
   
# In above Case, it is giving same value for Father also as 2 Lakhs
# when we gave Property as same Attribute in both class

# In this Example, Parent Class is having Constructor and child class is also having constructor. 
# So, Constructor Overriding is Happening.
# To Avoid it, We use super() --> super.__init__(), super().__init__(args), super().method()   (Method Overriding)

'''

# Explanation of Inheritance 




