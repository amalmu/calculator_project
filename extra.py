# binary no to decimal conversion

# binary=list(input("ENTER BINARY vALUE: "))
# dec=0
# for i in range (len(binary)):
#     dig=binary.pop()
#     if dig==1:
#         dec=dec+pow(2,i)
# print("DECIML VALUE IS: ",dec)

# n=input("ENTER A BINARY NO: ")#1111
# l=list(n)
# sum=0
# # print(l)
# l.reverse()
# print(l)
# for i in range(len(l)):
#     sum=sum+int(l[i])*2**i
#     #15
# print("THE DECIMEL NO IS: ",sum)

# pattern 

# row=5
# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(row,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

  

# row=5
# for i in range(1,6):
#     for j in range(i):
#          print(" ",end="*")
#     print()
   
# for i in range(row-1,0,-1):
#     for j in range(i):
#           print(" ",end='*')

#     print()



# row=5
# for i in range(1,6):
#     for j in range(row-4,4):
#         print("*",end=" ")
#     for k in range(i):
#         print("*",end=" ")
# print()
# for i in range(row-1):
#     for j in range(2-i,2):
#         print(' ',end=" ")
#     for k in range(1,row):
#         print("*",end=" ")
         
# print()


print("SELECT FROM THE MENU")
print('''1=NON-VEG
2=VEG''')
option=int(input("ENTER UR CHOIC: "))
fud=""

if option==1:
    print("YOU HAVE A GREAT TASTE IN NON VEG")
    print('''a=chinese
b=arabian
c=latin''')
    
    item=input("ENTER YOUR STYLE OF FUD")
    if item=='a':
        print("YOU CHOSE CHINESE AND SELECT UR PREFEREED FUD")
        fud=input("ENTER UR FUD: ")
        print("YOUR FUD IS",fud)
    elif item=="b":
        print("YOU CHOSEN ARABIAN DISH")
        fud=input("ENTER UR FUD: ")
        print("THE FUD IS",fud)
    elif item=="c":
        print("YOU CHOSE LATIN FUD")
        fud=input("ENTUER UR FUD: ")
        print("Enjoy your",fud)
    else:
        print("INVALID CHOICE")
elif option==2:
    print("YOU ARE A VEGAN AND VEG IS THE BEST CHOICE")
    print('''x=VEG SOUP
y=salad
m=payasam''')
    ros=input("ENTER YOUR NONVEG CHOICE: ")
    if ros=="x":
        print("YOUR FOOD IS VEG SOUP AND ENJOY iT")
    elif ros=='y':
        print("U HAVE CHOSEN SALAD AND KEEP IT")
    elif ros=='m':
        print("YOU ARE A SUGAR LOVER AND ENJOY PAYASAM")
    else:
        print("INVALID CHOICE")

    
    

    

    
