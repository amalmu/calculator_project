# a=[1,2,3]
# b=[4,5,6]
# c=[6,5,4]
# out=[]
# for i in range(1):
#     out.append(a)
#     print(out)
# for j in range(1):
#     out.append(b)
#     print(out)
# for k in range(1):
#     out.append(c)
#     print(out)
# # print(out,"\n")

# row=[]
# col=[]
# ba=[]
# for i in range(3):
#     row.append(i)
# for j in range(3):
#     col.append(i)
# for k in range(3):
#     ba.append(i)
# print(row)
# print(col)
# print(ba)
# print()

# matrix using list
# mat=[]
# for i in range(3):
#   row=[]  
#   for j in range(3):
#     a=int(input("ENTER NUMBER: "))
#     row.append(a)
#   mat.append(row)
# for i in mat:
#   print(i)
  
# matrix using string
# mat=[]
# for i in range(3):
#   row=""
#   for j in range(3):
#     a=input("ENTER NUMBER: ")
#     row+=a+" "
#   mat.append(row)
# for i in mat:
#   print(i)
  
# a = input("ENTER CHAR: ")

# result = ""
# i = 0

# while i < len(a):
#     count = 1
#     while i + 1 < len(a) and a[i] == a[i + 1]:
#         count += 1
#         i += 1
#     result += str(count) + a[i]
#     i += 1

# print(result)





# a =input("ENTER THE STRING: " )
# count = 1
# new = ""
# for i in range(1, len(a)):
#     if a[i]==a[i-1]:
#         count+= 1
#     else:
#         new+=str(count)+a[i-1]
#         count=1
# new+=str(count)+a[i-1]
# print(new)

