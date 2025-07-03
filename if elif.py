num=int(input("enter the days"))
if num<=5:
    print("the charge is",num*2)
elif num>=6 and num<=10:
    print("the charge is",num*3)
elif num>=11 and num<=15:
    print("the charge is",num*4)
elif num>15:
    print("the charge is",num*5)
else:
    print("wrong days selected")