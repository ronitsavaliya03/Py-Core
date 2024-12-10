num=(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

idx=0
n=25

# while(idx<len(num)):
#     if(n==num[idx]):        
#         print("Found at index",idx,"\nnumber is",num[idx])
#     else:
#         print("Finding...")
    
#     idx+=1


i=0

# while(i<=10):
#     if(i%2==0):
#         i+=1
#         continue
#     else:
#         print(i)

#     i+=1


# for j in num:
#     if(n==j):
#         print("Found at",idx)
#         break
#     idx+=1


n= int(input("Enter the number:"))

# for i in range(1,11):
#     print(n*i)

for i in range(1,n):
    n*=i

print(n)
