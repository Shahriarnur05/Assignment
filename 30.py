def sumOfDigits(n):
    sum = 0
    rem = 0
    while(n>0):
        rem = n%10
        sum = sum + rem
        n = n // 10

    return sum

x = int(input("Enter a number: "))


print("Sum of Digits = ",sumOfDigits(x))