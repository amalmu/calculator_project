# # REVERSE A STRING
# a=input("Enter a string: ")
# rev=""
# for i in a:
#     rev=i+rev
# print(rev)

# # length of string
# a=input("ENTER A string: ")
# length=0
# for i in a:
#     length=length+1
# print(length)

# word count

# a=(input("ENTER A STRING   "))
# count=1
# for i in a:
#     if i==" ":
#       count=count+1
# print(count)
 


# printing patters 

# 1 rightt triangle

# row=5
# for i in range(1,row+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# square

# row=3
# for i in range(3):
#     for j in range(3):
#         print("*",end=" ")
#     print()

# triangle
# row=5
# for i in range(5):
#     for j in range(5-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
#     print()


# row=5
# for i in range(5):
#     for j in range(2*i+1):
#         print(" ",end=" ")
#     for k in range(5-i-1):
#         print("*",end=" ")
#     print()


# row=5
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# row=5
# for i in range(1,row+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()


# row=5
# for i in range(5):
#     for j in range(5-i):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
#     print()


# row=5
# for i in range(5):
#     for j in range(row-i):
#         print(" ",end=" ")    
#     for k in range(2*i+1):
#         print("*",end=" ")
#     print()
# for i in range(row-1,0,-1):
#     for j in range(row-i+1):
#         print(" ",end=" ")
#     for k in range(2*i-1):
#         print("*",end=" ")
#     print()

# row=5
# for i in range(1,row+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

row=5
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(row-1,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()


# row=5
# col=5
# for i in range(row):
#     for j in range(col):
#         if i==0 or i==row-1 or j==0 or j==col-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
    # print()
#      not needed but refer
#    print("*",end=" ")
#     print()
# for i in range(1,row+1):
#     for j in range(i,i+1):

#         print("*",end=" ")
#     print()


# a=input("ENTER THE STRING: ")
# max=0
# count=0

# for i in a:
#     if i==0:
#         print(max(i))
    
#     print(count)
#     # print(str(len(a)))