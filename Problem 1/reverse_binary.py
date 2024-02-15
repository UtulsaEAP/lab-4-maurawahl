"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name: Maura Wahl
Lab Time: Thursdays at 2

"""


def reverse_binary():
    user_num = int(input())
    first_output = 0
    # YOUR CODE HERE
    s=""
    while user_num >0:
        first_output = user_num%2
        s += str(first_output)
        user_num = int(user_num/2)
    print(s)
if __name__ == "__main__":
    reverse_binary()