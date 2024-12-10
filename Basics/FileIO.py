# file=open("demo.txt","w+")
# data=file.write("asdf")
# print(file.read())
# file.close()

    
# with open("demo.txt","w") as file:
#     file.write("Hi everyone\nwe are learning I/O\n")
#     file.write("using Java\nI like programming in Java")

# with open("demo.txt","r") as file:
#     data=file.read()

# newData=data.replace("Java","Python")
# print(newData)

# with open("demo.txt","w") as file:
#     file.write(newData)

import os
# os.remove("demo.txt")

def checkForWord():
    word="Python"
    with open("demo.txt","r") as file:
        data=file.read()
        if(data.find(word)!=-1):
            print("Found")
        else:
         print("Not found")

def checkByLine():
    word="Pyq"
    data=True
    LineNo=1
    with open("demo.txt","r") as file:
        while data:
            data=file.readline()
            if(word in data):
                print(LineNo)
                return
            LineNo+=1

    return -1

with open("num.txt","r") as file:
    count=0
    data=file.read()

    nums=data.split(", ")

    for val in nums:
        if(int(val)%2==0):
            count+=1

    print(count)

