def n_s(n,c):
    if n > 40 and n < 0:
        print("Invalid Number")

    else:
        for i in range (1,n+1): 
            print(f"Enter the number of students#{i}") #1,

            if c > 6 and c<0:
                print("Invalid Course")
            
            else:         # course 3
                total_cgpa = 0
                for j in range (1 , c+1):   
                    cgpa = float(input(f"Enter the cgpa of course#{j} = ")) #2
                    total_cgpa += cgpa   #9.7
                avg = total_cgpa / c   #9.7 / 3
        
            print(f"Average CGPA of studenttuu{i} is {avg} ")

n = int(input("Number of students: "))
c = int(input("Number of courses: "))

n_s(n,c)
