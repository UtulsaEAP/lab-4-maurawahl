"""
Complete the following python code to take in a list of values from the user and then normalize them

Name: Maura Wahl
Lab Time: Thursdays at 2 pm
"""

def norm():
    # Write your code here
    print(5)
    amount = int(input())
    numlist =[]
    for x in range(amount):
        number = input()
        numlist.append(float(number))
    largest =max(numlist)

    for x in numlist:
        newvalue = x/largest
        print(f'{newvalue:.2f}')
    

       

    pass
if __name__ == "__main__":
    norm()