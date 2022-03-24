'''
7. Write a python program that takes a positive integer number from 
the user and compute a sum of consecutive integers.

S#	Input	Output
(i)	Enter a positive integer: 8	The sum of the first 8 integers is 36
(ii)	Enter a positive integer:100	The sum of the first 100 integers is 5050
'''

n = int(input("Enter a positive integer: "))
sum = 0
if (n > 0):
    for i in range(1,n+1):
        sum = sum+i
print(sum)
