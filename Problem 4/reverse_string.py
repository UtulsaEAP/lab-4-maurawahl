"""
Complete the following python code to reverse the string entered by the user.

Name: Maura Wahl
Lab Time: Thursdays at 2 pm
"""

def reverse_string():
    # YOUR CODE HERE
    word = str(input())
    while len(word)>=1 and word != "done" and word != "Done" and word != "d":
        print(word[::-1])
        word = str(input())
    pass
if __name__ == "__main__":
    reverse_string()