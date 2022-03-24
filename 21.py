'''
import math
x , y = [int (x) for x in input("Enter two numbers: ").split()]

r = [x,y]
r.sort()
print (math.gcd(r[0], r[1]))


'''