class Student:
    def __init__(self,name):
        self.name=name


# s1=Student("radhika")

# print(s1.name)
# del s1
# print(s1.name)

class Account:
    def __init__(self,accNo,accPassword,bal):
        self.balance=bal
        self.accNo=accNo
        self.__accPassword=accPassword

    def debit(self,amount):
        self.balance-=amount
        print("Rs.",amount,"was debited")
        print("Current balance=",self.balance)
    
    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"was credited")
        print("Current balance=",self.balance)

    def __balance(self):
        return self.balance
    
    def resetPassword(self):
        print(self.__accPassword)

acc1=Account("1658496","asdf",1000000)
# acc1.resetPassword()
# acc1.__balance()


class Car:
    def __init__(self,type):
        self.acc=False
        self.brk=False
        self.clutch=False
        self.type=type

    # @staticmethod
    def start(self):
        self.clutch=True
        self.acc=True
        print("Car started...")

    @staticmethod
    def stop():
        print("Stop car.")

class Toyota(Car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)
        super().start()

class Fortuner(Toyota):
    def __init__(self, type):
        super().__init__(type)

# car1=Toyota("fortuner","electical")
# car2=Toyota("prius")

# print(car1.type)
# car1.start()

class A:
    varA="welcome to class A"

class B:
    varB="welcome to class B"

class C(A,B):
    varC="welcome to class C"

c1=C()
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)




class Person:
    name="anonymous"

    def changeName(self,name):
        Person.name=name

    @classmethod
    def changeNameByClsMethod(cls,name):
        cls.name=name


p1=Person()
p1.changeName("ronit")

# print(p1.name)
# print(Person.name)


class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math

    # def calcPercentage(self):
    #     self.percentage=str((self.phy+self.math+self.chem)/3)+"%"

    @property
    def percentage(self):
        return str((self.phy+self.math+self.chem)/3)+"%"        

# stu1=Student(98,68,76)
# # stu1.calcPercentage()
# print(stu1.percentage)

# stu1.phy=86
# # stu1.calcPercentage()
# print(stu1.percentage)


class Complex:
    def __init__(self,real,img) -> None:
        self.real=real
        self.img=img

    def showNumber(self):
        print(self.real,"i + ",self.img,"j",sep="")

    #dunder function
    def __add__(self,num2):
        newReal= self.real+num2.real
        newImg= self.img+num2.img
        return Complex(newReal,newImg)
    
    def __sub__(self,num2):
        newReal= self.real-num2.real
        newImg= self.img-num2.img
        return Complex(newReal,newImg)



num1=Complex(1, 3)
num1.showNumber()

num2=Complex(4, 6)
num2.showNumber()

num3=num1+num2
num3.showNumber()

num3=num1-num2
num3.showNumber()