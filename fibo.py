n = int(input("Enter the maximum value for Fibonacci sequence : "))

x = 0
y = 1

if (n<0):
    print("Please Enter a positive number")
else:
    while y<(n+1):
        print(y)
        x = y
        y = x+y
