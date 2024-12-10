light=input("Enter your light: ")

if(light=="red"):
    print("Stop!")
elif(light=="yellow"):
    print("Wait..")
elif(light=="green"):
    print("Go go")
else:
    print("Signal poll is under construct")


a=int(input("Enter the num1:"))
b=int(input("Enter the num2:"))
c=int(input("Enter the num3:"))

if(a>=b and a>=c):
    print(a)
elif(b>=c):
    print(b)
else:
    print(c)


if(a%7==0):
    print("Multipal of 7")
else:
    print("Not Multpal of 7")


list=[8,9,3,6,5,4,1]

list.append(7)
print(list)

list.sort()
list.insert(1,2)
print(list)
list.sort(reverse=True)
print(list)