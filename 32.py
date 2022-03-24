'''
32. Write a function named isPrime that checks if a numer is prime or not. If the number is prime the function 
returns true, otherwise false.

For example, the call of isPrime(11) should return true

Prime number: A number that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11).'''

def isPrime(x):
    for i in range (2 , x):
        y = x % i+1
        if (y == 0):
            return "False"
            break
        else:
            return "True"
            break
        

x = int(input("Enter a number: "))
print(isPrime(x))
