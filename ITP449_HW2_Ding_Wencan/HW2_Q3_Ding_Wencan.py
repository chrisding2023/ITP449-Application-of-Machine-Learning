# Ding Wencan
# ITP449 Spring 2022
# HW2
# Question 3
def valid(password):
    if(len(password)<8):
        return False
    if(True):
        count = 0
        number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for letter in password:
            if letter in number:
                count = 1
        if count == 0:
            return False
    if (True):
        count = 0
        special = ["!","@", "#", "$"]
        for letter in password:
            if letter in special:
                count = 1
        if count == 0:
            return False
    if (True):
        count = 0
        for letter in range(65, 91):
            if chr(letter) in password:
                count = 1
        if (count == 0):
            return False
    if (True):
        count = 0
        for letter in range(90, 123):
            if chr(letter) in password:
                count = 1
        if (count == 0):
            return False
    return True
T = True
while T == True:
    password = input("Password: ")
    if (valid([letter for letter in password])):
        print("Access Granted!")
        T = False
    else:
        print("Invalid password. Try again!")
        print("The password must be at least 8 characters long.")
        print("The passwrod must contain both uppercase and lowercase letters.")
        print("The password must contain at least one number between 0-9.")
        print("The passowrd must contain a special character: !, @, #, $.")





