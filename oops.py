class Student:
    college_name = "B V D U C"
    def __init__(self):                       # this is default consntructor..if user does not make one...python itself creates default constructor
        pass                                  # so default constructor is without any arguments other than self
    
    def __init__(self,name,age):                              
        print("new student is created")          #just to show that init method is called by default as soon as object is initiated
        print(self)                              #self point to the current instance of the class..point to object that is being created
        self.name = name                         #<__main__.Student object at 0x000001AFEEAB5D60> is printed which is student1 in our case
        self.age = age
        #print("name is " + self.name)
        
    def welcome(self):                          #whether we use self or not, self is the first argument in method
        print("welcome students", self.name)
        
    def get_age(self):
        return self.age   
    
    @staticmethod                            #static method are class level method which takes no self parameter, object se koi matlab nahi hai
    def hello():
        print("hello this is static method")     
        
        
        
                                                
student1 = Student("rahul",21,)                                 
print(student1.college_name)   
student1.welcome()
print(student1.get_age())  
student1.hello()               


# we can directly change attribute for object like student1.name = "tony"
# there are 2 types of attributes
# 1) class attributes   which is common to whole class
# 2) instance attribute   which belong to particular object, different for every object  self.name in init method is object attribute
# so logic is that if college is same for all the students we wont save college name seprately for every student which will take lot of space instaed we can
# make this college a class attribute(common to all)  
# we can also have same class and object attribute like we can provide name as class attribute also but object attribute will have more weightage than class attribute 
# one use case for class attribute is that if there is name = "anonymous" under Student class and any object of student doesnt have name ...anonymous
# will be set by default   


# four pillars of oops are abstraction, encapsulation, inheritance, polymorphism

class Car:
    def __init__(self):
            self.acc = False
            self.clutch = False
            self.brk = False
        
    def start(self):
        self.acc = True
        self.clutch = True
    
    
car = Car()
print(car.clutch)      #print false
car.start()    
print(car.clutch)      #print true

#ABSTRACTION ------>  abstraction is a concept in which we hide implementation details of a class 
# and only show essential features to the user

#del keyword -----> used to delete objects
print(car)
# del car
# print(car)      #nameError 
del car.clutch
#print(car.clutch)      #we can also delete attribute of object, will give AttributeError: 'Car' object has no attribute 'clutch'



# PRIVATE ATTRIBUTES AND MWTHODS
# Private attributes and methods are meant to be used only within the class and are not accessible outside the class
# to make private just put double underscore before attribute or method

class Person:
    __name = "anonymous"
    
    def __hello(self):
        print("this is private method")
        
    def welcome(self):                                #this can internally access the private hello function
        self.__hello()    
        
        
p1 = Person()
# print(p1.__name)      #both this line will give attribute error because of being private
# print(p1.__hello()) 
p1.welcome()    

# we make private functions beacuse they can not be used by objects , but such functions are internally used by other functions


# GETTERS AND SETTERS
# A getter is a method that retrieves the value of an attribute from a class. It provides read access to the attribute while controlling 
# how it is accessed. Getters typically have names prefixed with get_ or directly use the attribute name.
class Person:
    def __init__(self,name):
       self.__name = name
       
    def get_name(self):
        return self.__name
    
    def set_name(self,newName):
        self.__name = newName
    
per2 = Person("john")
#print(per2.name)
print(per2.get_name())
per2.set_name("john wick")
print(per2.get_name()) 





# INHERITANCE ----> Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class. Child class is the class that inherits from another class, 
# also called derived class.

# three types of inhertitance are single, multilevel and multiple inheritance

class Car:
    colour = "black"
    @staticmethod
    def start(carName):
        print(carName + " has started")
        
class Toyota(Car):
    brand = "toyota"
    def __init__(self,name):
        self.name = name       
        
        
car1 = Toyota("fortuner")
print(car1.name)         
car1.start(car1.name)     #start is not a toyota method but it has inherited car class therefore we are not getting error

class Fortuner(Toyota):
    def __init__(self,type):
        self.type = type
        
        
f1 = Fortuner("diesel")
print(f1.type)   
f1.start("f1")          #here f1 can access start method because of multi-level inheritance .Fortuner class inheriting from Toyota, Toyota class
                        #inheriting from Car class
                        

#MULTIPLE INHERITANCE
class A():
    varA = "this is class A"
    
class B():
    varB = "this is class B"                      
class C(A,B):
    varc = "this is class c "               
    

c1 = C()
print(c1.varc)
print(c1.varA)       #varA and varB are attributes of two parent classes which class C is inheriting from
print(c1.varB)          






#SUPER KEYWORD ---->   super() method is used to acccess methods of parent class

class Car():
    def __init__(self,type):
        self.type = type
        
    @staticmethod
    def start():
        print("car started from parent class")
        
    @staticmethod
    def stop():
        print("car stopped")   
        
        
class ToyotaCar(Car):
    def __init__(self,name,type):
        self.name = name
        super().__init__(type)          #calling constructor of parent class(Car)
        super().start()                 #calling method of parent class(Car)
        
        
car12 = ToyotaCar("hyryder","diesel")        
print(car12.type,car12.name)





# CLASS METHOD ------>    a class method is bound to the class and receives the class as an implicit argument
# Note- static method can't access or modify class state and generally used for utility. 



class Person:
    name = "anonymous"
    
    # def change_name(self,name):    #basically what we want to do is change class attribute of Person i.e. name...there are many ways
    #     self.name = name
    #     #Person.name = name
    #     self.__class__.name = "rahul"
        
    @classmethod
    def change_name(cls,name):     #class method directring accessing and modifying class attribute
        cls.name = name    
        



per1 = Person()
per1.change_name("rahul")
print(per1.name)  
print(Person.name)






# PROPERTY ----> we use @property decorator on any method in the class to use method as a property
# jab ek attribute ki value function pe depend kr rhi hh to function ko he attribute bna do
class Student():
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        #self.percentage = (self.phy+self.chem+self.math)/3
        
    # def cal_per(self):
    #     self.percentage = (self.phy+self.chem+self.math)/3
    
# the problem here is if we change one subject marks the percentage does not change , it remain same which was at the time of object creation
# so we can make a method to calculate percentage and call it with new values, but best way is to use property decorator which sets method as attribute
#automatically update the required value

    @property
    def percentage(self):                           #jase he kisi bhi attribute me change hoga automatically method run hoga aur return value change hogi(lastest value is considered for calculation)
        return (self.phy+self.chem+self.math)/3
    
        

# stu1 = Student(67,98,54)
# print(stu1.percentage)  
# stu1.phy = 98
# print(stu1.percentage)          no change in percentage despite changing phy value

stu1 = Student(67,98,54)
print(stu1.percentage)  
stu1.phy = 98
print(stu1.percentage) 







# PLOYMORPHISM -----> In Python, polymorphism is a core principle of object-oriented programming (OOP). It refers to the way in which different
# object classes can share the same method name, but those methods can act differently based on which object calls them. There are two main 
# types of polymorphism in Python:

# 1)Method Overriding (Run-time Polymorphism):
# This occurs when a child class inherits a method from a parent class but provides a specific implementation of that method in the child class.
# The method in the child class overrides the method in the parent class.

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Polymorphism via method overriding
animals = [Dog(), Cat()]
for animal in animals:
    animal.sound()


