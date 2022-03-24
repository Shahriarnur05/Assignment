'''
16.Write a python program that displays the following series 
and computes its sum. Display all the terms and the sum. 
Make sure there is no extra plus sign at the end.

Series: 2+4+8+16+...+1024 = ?'''

sum = 0
n=1
while (0<n<1024):
    n = 2*n
    print(n,end= "")
    if (n != 1024):
        print(end="+ ")

    sum = sum + n
    
print(" =",sum)



