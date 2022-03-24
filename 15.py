'''
**15.Write a python program that uses a loop to compute and 
prints the sum of a given number of squares. For example, 
if 5 is input, then the program will print 55, 
which equals $1^2 + 2^2 + 3^2 + 4^2 + 5^2$.**'''

n = int(input("Enter a integer number: "))
sum = 0

for i in range (1, n+1):
    sum = sum + i**2
    
print(sum) 
