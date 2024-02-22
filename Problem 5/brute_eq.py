"""
Complete the python code to find the solution to the system of linear equations entered by the user. 
The equations are of the form ax + by = c and dx + ey = f. The solution should be printed in the form x = # and y = #. 
If there is no solution, print "There is no solution".

Name: Maura Wahl
Lab Time: Thursdays at 2 pm
"""

def brute_eq():
    #Read in first equation, ax + by = c 
    a = int(input())
    b = int(input())
    c = int(input())

    #Read in second equation, dx + ey = f
    d = int(input())
    e = int(input())
    f = int(input())

    #x=0
    #y=0
    solution_flag = False
    # YOUR CODE HERE
    for x in range(-10,11):
        for y in range(-10,11):
            #if -10<=a<=10 and -10<=b<=10 and -10<=d<=10 and -10<=e<=10:
            if a*x + b*y == c and d*x + e*y ==f:
                    solution_flag = True
            else:
                exit

    if solution_flag:
        x=int(((b*f)-(e*c))/((b*d)-(e*a)))
        y=int((c-(a*x))/b)
        print("x = " + str(x) + " , y = " + str(y))
    else:
         print("There is no solution")
if __name__ == "__main__":
    brute_eq()