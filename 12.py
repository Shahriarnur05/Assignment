'''
12.Write a python program that takes a positive integer from 
the user and determines whether an input is prime or not. 
A prime number is a positive integer divisible by exactly 
two numbers, 1 and the number itself.

S#	Input	Output
(i)	Enter a number: 5	Prime
(ii)	Enter a number: 1	Not Prime
(iii)	Enter a number: 2	Prime'''

n = int(input("Enter a number: "))

for i in range (2,n):
    if (n % i==0):
        print("Not Prime.")
        break

if (n == 1):
    print("Not Prime")

elif (n % i !=0):
    print("Prime.")