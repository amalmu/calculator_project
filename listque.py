# 1) Given 2 list .
# A = [ 1, 2, 3, 4, 5 ]
# B = [ 3, 4, 5, 6, 7, 8]
# Write a program to merge these two list and arrange them 
# in ascending order.Only distinct value should be there in 
# list.
# Out put : [ 1, 2, 3, 4, 5, 6, 7 ,8]


# a= [ 1, 2, 3, 4, 5 ]
# b= [ 3, 4, 5, 6, 7]
# c=a+b
# y=set(c)
# print(list(y))#this is the simple method  for thiwss question


#another method for the same ques using loop as the previous one 
# will not work if the elements are not in ascending order    (Bubble sort)
# a= [8,2,4,2,1]
# b= [8,6,9,2,1]
# c=a+b
# d=[]
# for i in c:
#     for j in d:
#         if i==j:
#             break
#     else:
#         d+=[i]

# for i in range(len(d)):
#     for j in range(len(d)-1):
#         if d[j]>d[j+1]:
#             d[j],d[j+1]=d[j+1],d[j]
# print(d)
    



# 2)Write a program to find the missing elements in a list .
# The Given list will have distinct numbers from 1 to n.
# n being whole number


# a=[1,4]
# n=4
# l=[]
# for i in range(1,n):
#     if i not in a:
#         l+=[i]
        
# print(l)


# 3)Give#ection of the list 
# # Output : [ 3, 4, 5 ]
# a=[1,2,3,4]
# b=[3,4,5]
# c=[]
# for i in a:
#     for j in b:
#         if i==j:
#             c+=[i]
# print(c)