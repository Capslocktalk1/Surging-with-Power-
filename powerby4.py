def powerFour(n):
    count = 0
    if (n&(~(n&(n-1)))):
        while(n > 1):
            n>>=1
            count += 1
        if (count%2==0):
            return 1
        else:
            return 0
        
a = int(input("Enter a number: "))

if powerFour(a):
    print("The number is power of four")
else:    
    print("The number is not power of four.")