# as normally we use
# def sq(n):
#     n=n**2
#     return n

# print(sq(3))


# using lambda function

# sq=lambda n:n**2
# print(sq(3))
# # or
# v=3
# print(sq(v))

# sm=lambda a,b,c:a+b+c
# a,b,c=2,1,3
# print(sm(a,b,c))

# sn=lambda a,b:a+b
# print(sn(2,3))

# different function in lambda

# # filter()
# a=[1,2,3,4,5,6,7,8,9,10]
# b=list(filter(lambda u:u%2!=0,a))
# print(b)


# # map()
# a=[1,2,3,4,5]
# b=list(map(lambda x:x**3,a))
#  print(b)

# # reduce ()
from functools import reduce
a=[1,2,3,4,5]
b=reduce(lambda x,y:x+y,a)
print(b)

# myse={1,2,3,4}
# b=reduce(lambda x,y:x+y,myse)
# print(b)
