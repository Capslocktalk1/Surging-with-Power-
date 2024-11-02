def powerEight(n):
    count = 0
    if (n & (n - 1)) == 0:
        while n > 1:
            n >>= 1
            count += 1
        if count % 3 == 0:
            return 1
    return 0

a = int(input("Enter a number: "))

if powerEight(a):
    print("The number is a power of eight.")
else:    
    print("The number is not a power of eight.")
