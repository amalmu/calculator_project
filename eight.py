# #REVERSE A STring

# a=str(input("ENTER A STRING: "))
# rev=""
# count=len(a)
# while count>0:
#     rev+=a[count-1]
#     count-=1
# print(rev)


# #SUM OF N NATURAL NUMBERS

# a=int(input("ENTER THE LIMIT: "))
# sum=0
# while a>0:
#     sum=sum+a
#     a-=1
# print(sum)

#FIBONACCCI SERIES

n=int(input("ENTER THE LIMIT: "))
a=0
b=1
i=0
while i<n:
    print(a)
    # a=b
    # b=a+b
    a,b=b,a+b
    i+=1


# n=int(input("ENTER THE NUMBER: "))
# multi=1
# i = 1
# while i <= 10:
#     # print(f"{n} x {i} = {n * i}")
#     print 
#     i += 1
#     print(multi)


# for i in range(11):
#     print(i)