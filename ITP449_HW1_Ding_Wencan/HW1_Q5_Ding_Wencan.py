#Ding_Wencan
#ITP 449
#HW1
#Question 5
name = input("What is your name? ")
if name.lower() == name.lower()[::-1]:
    print(name,",your name is a palindrome!")
else:
    print(name,",your name is not a palindrome!")
