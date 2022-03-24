'''
8. Write a python program that takes a positive integer 
number from the user and compute a sum of reciprocals.

The sum of reciprocals,
sum=1+1/2+1/3+⋅⋅⋅+1/n'''

sum = 0
x = int(input("Enter a positive integer: "))
if (x > 0):
    for i in range (1,x+1):
        b = 1 / i
        sum = sum + b

print(sum)