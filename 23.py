'''
23.Write a python program that takes a number from the user and checks if it 
is a perfect number. A perfect number is a positive integer that is equal to the 
sum of its positive divisors excluding the number itself. 28 is a perfect 
number because the sum if its divisors 1+2+4+7+14 is equal to 28'''

n = int(input("Enter a number: "))
sum = 0
for i in range (1, n):
    if (n%i == 0):
        sum = sum + i
y = sum 

if (y == n ):
    print("Perfect.")
else:
    print("Not perfect.")