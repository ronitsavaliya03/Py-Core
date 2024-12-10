list=[]


list.append(int(input("Enter the num1: ")))
list.append(int(input("Enter the num2: ")))
list.append(int(input("Enter the num3: ")))
list.append(int(input("Enter the num4: ")))
list.append(int(input("Enter the num5: ")))

tempList=list.copy()
tempList.reverse()


if(tempList==list):
    print("List is Palindrome")
else:
    print("Not Palindrome")

grade=("A","A","C","B","C","B","B","A")

print("number of students who have A grade: ",grade.count("A"))
print("number of students who have B grade: ",grade.count("B"))
print("number of students who have C grade: ",grade.count("C"))

demo=["A","A","D","B","C","G","B","E"]

demo.sort()

print(demo)

dictionary={
    "cat": "a small animal",
    "table":["a piece of furniture","list of facts & figures"]
}

print(dictionary)

marks={}

x=int(input("Enter the marks:"))
marks.update({"phy":x})

x=int(input("Enter the marks:"))
marks.update({"chem":x})

x=int(input("Enter the marks:"))
marks.update({"math":x})

print(marks)

