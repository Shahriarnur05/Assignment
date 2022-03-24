'''
14.Write a python program that takes
5 numbers from the user and finds their average(you must use a loop)'''

sum = 0
print("Enter 5 numbers: ")
for i in range (1 , 6):
    
    x = float(input(f"{i}: "))
    sum = sum + x
avg = sum / 5
print(avg)