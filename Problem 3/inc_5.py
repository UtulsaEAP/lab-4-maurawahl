"""
Complete the following python code to print all numbers between the two values incrementing by 5 from the initial value to the final value. The initial value and final value are entered by the user. If the final value is less than the initial value, print "Second integer can't be less than the first.

Name: Maura Wahl
Lab Time: Thursdays at 2 pm
"""

def inc_5():
    # Write your code here
    print("What is the first number?")
    first_number = int(input())
    print("What is the second number?")
    second_number = int(input())

    if second_number >= first_number:
        for x in range(first_number, second_number+1, 5):
            print(x, end=" ")            
    else:
        print("Second integer can't be less than the first.")
    pass



if __name__ == '__main__':
    inc_5()