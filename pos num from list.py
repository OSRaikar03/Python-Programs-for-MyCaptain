numList = []
n = int(input("Enter the list size : "))

print(" ")
for i in range(0, n):
    print("Enter number at position ", i+1, ":")
    item = int(input())
    numList.append(item)

print(" ")
print("The User List is ", numList)

print(" ")
print("The positive number(s) are : ")

for num in numList: 
      
    if num >= 0: 
       print(num, end = " ") 
