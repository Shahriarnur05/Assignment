def factorial(n):
    a = 1
    for i in range (n , 1, -1):
        a = i * a
    print(a)

n = int(input("Enter a integer number: "))
factorial(n)
