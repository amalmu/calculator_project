# input values in a list
# a=[]
# for i in range(5):
#     n=int(input("ENTER THE NUMBER: "))
#     a.append(n)
# print("The list is ",a)


# reverse a list

# a=[2,4,6,8,9]
# a.reverse()
# print(a)

# rev=[]
# for i in range(len(a)-1,-1,-1):
#     rev.append(a[i])
# print(rev)

# count 
# a=[2,8,5,7,9,7,5,4]
# count=0
# for i in a:
#     count+=1
# print("count=",count)

# a=[2,4,6,8]
# b=[]
# for i in range(len(a)):
#     b=a[i]*a[i]
#     a.append(b)
#     print(b)

# # a=[2,4,5,7]
# b=[]
# for i in a:
#     i=i**2
#     b.append(i)
# print(b)

# remove empty list
# a=[1,3,4,5,[]]
# for i in range(len(a)):
#     if a[i]==[]:
#         a.remove([])
# print(a)


# a=[2,5,10,3]        
# b=[]
# for i in a:
#     if i%5==0:
#       b.appen


# # sum of two list
# a=[2,4]
# b=[3,5]
# c=0
# for i in a:
#     c+=i
# for j in b:
#     c+=i
# print(c)


#separate pos and neg nos in a list

# a=[2,4,-1,-8] 
# pos=[]
# neg=[]
# for i in a:
#     if i > 0:
#         pos.append(i)
#     else:
#         neg.append(i)
# print(pos)
# print(neg)


# largetss numb

# a=[2,4,3,8,1]
# b=a[0]
# c=a[0]
# for i in a:
#     if i>a[0]:
#         b=i
# print(b)



# sort methdds
# a=[2,3,1,5]
# a.sort()
# print(a)


# # duplicate element
# a=[1,2,3,3,5,2,6,5]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)

# reverse each string 

# a=["mala","kama","vala"]
# rev=[]
# k=0
# for i in a:
#     k=i[::-1]
#     rev.append(i)
# print(rev)


# number to words

ones=["zero","one","two","three","four","five","six","seven","eight","nine"]
teen=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens=["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety","hundred"]

n=input("Enter a number: ")
if n.isnumeric():
    num=int(n)
    if 1<=num<=100:

        if 1<=num<=9:

          print(ones[num])
        elif 10<=num<=19:
          print(teen[num-10])
        elif num%10==0:
          print(tens[num//10])
        else:
           print(tens[num//10]+" "+ones[num%10])
    else:
       
       print("Number out of  range")
else:
   print("INVALID INPUT")
   