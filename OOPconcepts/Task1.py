""" code for student class where encapsulation is achieved using getter method """
class Student:
    
    def __init__(self,name, roll_number, grade):
        self.name = name
        self.rollnumber = roll_number
        self.grade = grade

    def get_details(self):
        # function to get data of student
        name = self.name
        rollno = str(self.rollnumber)
        grade = str(self.grade)
        data = "Name of student is : "+name+" Roll No is : "+rollno +\
              " Grade is : "+grade
        return data
        
    def promote(self):
        # function to increment grade of student by 1
        grade = int(self.grade)
        if grade < 10:
            grade = grade + 1
            self.grade = grade

student1 = Student("John Doe",101,"7")
print(student1.get_details())
student1.promote()
print("After promoting")
print(student1.get_details())


# Encapsulation
'''
Encapsulation refers to binding of data members and member functions of a perticular class.
Encapsulation does not allow direct access to variables as well as functions.
variables can be changed using methods of same class only , which ensures that variables are not changed accidentally.
variables are kept as protected members to achieve encapsulation(by prefexing the name with underscore "_").
Getter and Setter methods are used for accessing this variables.
example:

class Employee(self,basic,hra):
    self._basic = basic
    self._hra = hra

    def set_basic(self,basic):
        self._basic = basic

    def set_hra(self , hra):
        self._hra = hra
    
    def get_salary(self):
        salary = self._basic + self._hra
        return salary
employee1 = Employee(10000,5000)
employee1.get_salary()
'''

# Inheritance 
''' 
Inheritance is a OOP concept where access of data members and member functions of inherited class are given to
a class which is derived from it. 
this concept is mainly used for code reusability.
Python supports multiple inheritance where one class can be derived from multiple classes
example:

class A:
    def printA(self):
        print("Inside class A)

class B:
    def printB(self):
        print("Inside class B)

class C(A,B):
    def printC(self):
        print("Inside class C")

object = C()
print(object.printC())
print(object.printA())
print(object.printB())

'''

# polymorphism
'''
Polymorphism means having many forms.
In OOP when a function or an operator has 2 or more different behaviours its called as polymorphism.
a function or Operator being able to give 2 or more different outputs is called as polymorphism.
Polymorphism can be compile time or run time.
Polymorphism is achieved using Overloading and Overriding.
polymorphism can be achieved in Built in methods , Operators and user defined functions.
built in methods:
    len() methods will return length of string,list,dictionary.
opeators :
    + operator does addition of int but concatination of strings
user-defined functions:

class sendimage:
    def sendmessage():
        print("image sent")
    
class sendvideo:
    def sendmessage():
        print("video sent")

class sendtext:
    def sendmessage():
        print("text sent")
obj1 = sendimage()
obj1.sendmessage()
obj2 = sendvideo()
obj2.sendmessage()
obj3 = sendtext()
obj3.sendmessage()

same method sendmessage() behaves differently in all three classes.
'''