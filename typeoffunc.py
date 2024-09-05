# x=10
# def fun(x):
#     print(x,"inside the function")
#     print(y,"inside the function")
# y=10
# fun(x)   


# pass by vaalue
# -----------------
# immutable
#copy of the value
#modification with not affect orginal value

# def fun(x):
#     x+=10
#     print(x,"inside the fucntiojn")
# x=10
# print(x,"outside the function")
# fun(x)
# print(x,"outdide the function")
  
# pass by refernce
# -------------------

# mutable
#address location is passed
# modification inside trhe function will affect orginal value

# def ls(x):
#     x.append(4)
#     print(x,"inside the fun ction")
# x=[1,2,3]
# print(x,"outside the function")
# ls(x)
# print(x,"outside the function")

# def st(n):
#     if n>0:
#         return n+st(n-1)
#     else:
#         return 0
# print(st(5))

# def fac(n):
#     if n==0:
#         return 1
#     else:
#         return n*fac(n-1)
# print(fac(3))


def ra(n):
    rev=''
    count=len(n)
    if count>0:
        return rev+n[count-1]
    else:
        return 0
n=input("Enter the string: ")
print(ra(n))