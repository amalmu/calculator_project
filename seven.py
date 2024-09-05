# #SUM OF DIGITS

# num=int(input("ENTER A NUMBER: "))
# sum=0
# while num>0:
#     x=num%10
#     sum=sum+x
#     num=num//10
# print("THE SUM OF DIGITS ARE",sum)

#REVERSE OF DIGIT

# num=int(input("ENTER A NUMBER: "))
# rev=0
# length=len(str(num))
# while num>0:
#     x=num%10
#     rev=rev*10+x 
#     num=num//10
# print("REVERSE OF THE GIVEN DIGIT IS",rev)

#FACTORIAL

# num=int(input("ENTER A NUMBER: "))
# fact=1
# while num>0:
#     fact=fact*num
#     num-=1
# print("FACTORIAL IS",fact)


# #PALINDROME
# num=int(input("ENTER A NUMBER: "))
# rev=0
# pal=num
# while num>0:
#     x=num%10
#     rev=rev*10+x
#     num=num//10
# if pal==rev:
#     print("THEY ARE PALINDROME")
# else:
#     print("NOT PALINDROME")



# #ARMSTRONG
# n=int(input("ENTER A NUMBER: "))
# origin=n
# arm=0
# while n>0:
#     x=n//10
#     arm=arm+1

rows = 3

for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()

# rows = 3
# k = 0

# for i in range(1, rows + 1):
#     for space in range(1, rows - i + 1):
#         print(" ", end="")
    
#     while k != (2 * i - 1):
#         print("*", end="")
#         k += 1
    
#     k = 0
#     print()
