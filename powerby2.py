def powerTwo(n):
    if n == 0:
        return 0
    if ((n & (~(n-1))) == n):
        return 1
    return 0


a = int(input("Enter a Number: "))

if powerTwo(a):
    print("The number is the power of 2")
else:
    print("The number is not power of 2")