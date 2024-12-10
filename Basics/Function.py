def calc(a,b):
    return a+b


# print(calc(12,65))
# print(calc(82,68))
# print(calc(96,85))


def avgOfThree(a,b,c):
    return (a+b+c)/3


# print(avgOfThree(99,95,96))


cities= ["Jaipur","delhi","kolkata","banglore","pune","mumbai","raulkela","manoharpur"]


def printList(list):
    for item in list:
        print(item, end=" ")

    print()

# printList(cities)


def factorial(n):
    for i in range(n-1,1,-1):
        n*=i

    return n


# print(factorial(5))


def moneyConvertor(usd):
    inr = usd*83
    print(usd,"USD","=",inr,"INR")
    return inr


# moneyConvertor(73)


def oddEven(num):
    if(num%2==0):
        print("Even")
        return "even"
    else:
        print("Odd")
        return"odd"
    

# num=int(input("Enter the number: "))
# oddEven(num)



def fact(num):
    if(num==1 or num==0):
        return 1
    else:
        return num*fact(num-1)
        
    
# num2=int(input("Enter the number: "))
# print(fact(num2))


def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

# show(6)


def sumOfN(n):
    if(n==0):
        return 0
    else:
        return n+sumOfN(n-1)
    
# print(sumOfN(5))


def printElement(list, idx):
    if(idx==len(list)):
        return
    
    print(list[idx])
    printElement(list,idx+1)
    
printElement(cities,2)