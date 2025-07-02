"""
when the condition in "if"
block 
syntax :
if condition :
    statements
else:
    statements
    """

#checking the userid and password
userid = input("enter your userid")
password = input("enter your password")

if userid=="shakthi" and password=="parvathi@666":
    print("welcome to our netbanking of canara bank")

elif userid=="shiva" and password=="lakshmi@444":
    print("welcome to our netbanking of SBI bank ")
else:
    print("the userid and password is incorrect try again")