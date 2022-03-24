
def isPerfect(n):
    sum = 0
    for i in range (1, n):
        if (n%i == 0):
            sum = sum + i
    y = sum 

    if (y == n ):
        print("Perfect.")
    else:
        print("Not perfect.")


n = int(input("Enter a number: "))
isPerfect(n)

