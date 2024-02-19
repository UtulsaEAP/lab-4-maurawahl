"""
Complete the following python code to print the password entered by the user with the modifications described in the readme

Name: Maura Wahl
Lab Time: Thursdays at 2 pm
"""

def password_mod():
    print("What is your password")
    word = input()
    password = ''
    # Type your code here.
    passwordlist = list(word)
    x=0

    while len(passwordlist) > x:
        if passwordlist[x] == "i":
            passwordlist[x] = "1"
        elif passwordlist[x] == "a":
            passwordlist[x] = "@"
        elif passwordlist[x] == "m":
            passwordlist[x]  = "M"
        elif passwordlist[x] == "B":
            passwordlist[x] = "8" 
        elif passwordlist[x] == "s":
            passwordlist[x] = "$"
        else: passwordlist[x] == x
        password += passwordlist[x]
        x += 1

    print(str(password)+"!")
        
    

if __name__ == "__main__":
    password_mod()