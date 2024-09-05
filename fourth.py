# #month

# month=int(input("enter a number......"))
# if month==1:
#     print("January")
# elif month==2:
#     print("february")
# elif month==3:
#     print("March")
# elif month==4:
#     print("April")
# elif month==5:
#     print("May")
# elif month==6:
#     print("JUne")
# elif month==7:
#     print("JUly")
# elif month==8:
#     print("August")
# elif month==9:
#     print("september")
# elif month==10:
#     print("October")
# elif month==11:
#     print("NOvember")
# elif month==12:
#     print("december")
# else:
#     print("INVALID")


#day

# day=int(input("ENTER A NUMBER:"))
# if day==1:
#     print("MONDAY")
# elif day==2:
#     print("TUESDAY")
# elif day==3:
#     print("WEDNESDAY")
# elif day==4:
#     print("THURSDAY")
# elif day==5:
#     print("FRIDAY")
# elif day==6:
#     print("SATURDAY")
# elif day==7:
#     print("SUNDAY FUNDAY")
# else:
#     print("INVALID")


#Electiricity bill
units=int(input("ENTER THE UNITS:"))
if units<=100:
      bill=0
      print("THE CHARGE OF BILL IS 0")
elif units<=200:
      bill=(units - 100) * 5
      print("THE CHARGE OF BILL IS",bill)
else:
      bill=(5 * 100) + ((units - 200)*10)
      print("THE CHARGE OF BILL IS",bill)
    

#LARGEST OF THREE NUMBERS
# a=int(input("ENTER THE FIRST NUMBER:"))
# b=int(input("ENTER THE SECOND NUMBER:"))
# c=int(input("ENTER THE THIRD NUMBER:"))
# if a>b and a>c:
#     print(a,"IS LARGER")
# elif b>a and b>c:
#     print(b,"IS LARGER")
# else:
#     print(c,"IS LARGER")

#COST

# cost=int(input("ENTER THE COST OF BIKE:"))
# if cost>100000:
#    tax=cost*(15/100)
#    print("THE TOTAL TAX TO BE PAID IS",tax)
# elif cost>50000 and cost<100000:
#    tax=cost*(10/100)
#    print("THE TOTAL TAX TO BE PAID IS",tax)
# elif cost<=50000:
#    tax=cost*(5/100)
#    print("THE TOTAL TAX TO BE PAID IS",tax)
# else:
#    print("INVALID INPUT")