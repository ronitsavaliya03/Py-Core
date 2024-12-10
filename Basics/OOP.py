class Student:
    uni="Darshan University"

    #default constructor
    def __init__(self):
        print("Adding new student in database.")

    #parameterize constructor
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("Adding new student in database.")

    @staticmethod  #decorator
    def college():
        print("DIET")

    def welcome(self):
        print("welcome student,",self.name)

    def getAvg(self):
        sum=0
        n=0
        for val in self.marks:
            sum+=val
            n+=1
        print("hi",self.name,"your avg Score is:",sum/n)

# stu1=Student("tony",[83,92,39])
# stu1.welcome()
# stu1.getAvg()
# stu1.college()

# stu2=Student("arjun",[90,63,45])
# stu2.welcome()
# stu2.getAvg()

class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.clutch=True
        self.acc=True
        print("Car started...")


# car1=Car()
# car1.start()
        

class Account:
    def __init__(self,accNo,bal):
        self.balance=bal
        self.accNo=accNo

    def debit(self,amount):
        self.balance-=amount
        print("Rs.",amount,"was debited")
        print("Current balance=",self.balance)
    
    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"was credited")
        print("Current balance=",self.balance)

    def balance(self):
        return self.balance
    

# acc1=Account(45632697,100000)
# acc1.debit(5000)
# acc1.credit(10000)
# acc1.credit(25000)
# acc1.debit(7200)



        