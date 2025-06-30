#write a program to accept a number from 1 to 12 then display name of the month and days in that month like 1 for january and the no of days 31 and so on
mon_num=int(input ("enter a month number1 to 12.."))
if mon_num==1:
    print("january 31 days")
elif mon_num==2:
    print("feb 28 days")
elif mon_num==3:
     print("march 31 days")
elif mon_num==4:
    print("april 30 days")
elif mon_num==5:
    print("may 31 days")
elif mon_num==6:
    print("jun 30 days")
elif mon_num==7:
    print("july 31 days")
elif mon_num==8:
    print("aug 31 days")
elif mon_num==9:
    print("sep 30 days")
elif mon_num==10:
    print("oct 31 days")
elif mon_num==11:
    print("nov 30 days")
elif mon_num==12:
    print("dec 31 days")
else:
    print("wrong number selected")
