# def amal():
#     print("My name is Amal")
# amal()

# def sum(a,b):
#     sum=a+b
#     print("THE SUM IS",sum)
# sum(1,2)

# def sum(a,b):
#     sum=a+b
#     print("THE SUM IS",sum)
# a=int(input("ENTER FIRST NO: "))
# b=int(input("ENTER YOUR SECOND NO: "))
# sum(a,b)



# def div(a):
#     if a%2==0 and a%5==0 :
#         print("It is divisible by 2 and 5")
#     elif a%2==0 and a%5!=0:
#         print("DIVISIBLE BY 2 and not by5")
#     elif a%2!=0 and a%5==0:
#         print("ITS not DIVISIBLE by 2 and divisible by 5")
#     else:
#         print("Not divisible by both")
# a=int(input("ENTER YOUR NO: "))
# div(a)

# sides of a triangle

# def triangle(a,b,c):
#     if a==b and a==c:
#         print("The sides of the triangle are of an equilateral triangle")
#     elif a==b and a!=c:
#         print("The sides are of an isiceles triangle")
#     elif a!=b and b==c:
#         print("The sides are of an isoceles")
#     elif a!=b and a==c:
#         print("The sides are of an isoceles")
#     else:
#         print('ITS A NORMAL ONE')
# a=int(input("Enter 1st side: "))
# b=int(input("enter 2nd side: "))
# c=int(input("enter 3rd side: "))
# triangle(a,b,c)

# word count
# def word(a):
#     count=1
#     for i in a:
#         if i==" ":
#             count+=1
#     print(count)
# a=input("ENTER THE WORD: ")
# word(a)

# # letter count
# def let(a):
#     count=0
#     for i in a:
#         if i==i:
#             count+=1
#     print("COIUNT IS",count)
# a=input("Enter the string")
# let(a)
 

# factorial

# def yoh(a):
#     fact=1
    
#     for i in range(a):
#         if a>0:
#             fact=fact*a
#             a-=1
#     print("The factorial is",fact)
# a=int(input("Enter the no: "))
# yoh(a)

# using while loop
# def yoh(a):
#     fact=1
#     while a>0:
    
     
#         fact=fact*a
#         a-=1
#     print("The factorial is",fact)
# a=int(input("Enter the no: "))
# yoh(a)

# reverse a string

# def ful():
#     rev=""
#     a=input("ENTER THE STRING: ")
#     count=len(a)

#     while count>0:
#         rev=rev+a[count-1]
#         count=count-1
#     print(rev)

# ful()


# # sum of n natural no

# def nat():
#     sm=0
#     n=int(input("ENTER THE NO: "))

#     while n>0:
#         sm=sm+n
#         n=n-1
#     print(sm)

# nat()


# choice of operqtion

# def choice():
  
#     while True:
#         a=int(input("ENTER 1st no: "))
#         b=int(input("Enter 2nd no: "))
#         print('''
#     1= ADD
#     2=SUBTRACT
#     3=MULTIPY
#     4=DIVIDE'''
#           )
#         ch=int(input("enter ur choice: "))

#         if ch==5:
#             break
#         elif ch==1:
#             out=a+b
            
#         elif ch==2:
#             out=a-b
            
#         elif ch==3:
#             out=a*b
            
#         elif ch==4:
#             out=a/b
           
#         else:
#             print("INVALID")
#         print("the result is",out)
# choice()

# ones=['zero','one','two','three','four','five','six','seven','eight','nine']
# teen=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
# tens=['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety','hundred']
# def name():
#     n=int(input("enter your no: "))
#     if 1<=n<=100:
#             if 1<=n<=9:
#                 print(ones[n])
#             elif 1<=n<=19:
#                 print(teen[n-10])
#             elif n%10==0:
#                 print(tens[n//10])
#             else:
#                 print(tens[n//10]+" "+ones[n%10])
#     else:
#         print("INVALID")
# name()

# def details(name,place):
#     print("my name is",name,"and iam from",place) #positional argument
# details('vishnu','kottayam')
# details('kottayam','vishnu')
# details('vishnu','Anchal')

# details(place="kottayam",name="vishnu")#keyword Aruments
# details('kannur',name="vishnu")    
# details('kannur',place="vishnu")

# def detaila(name,age):
#     print("MY NAME IS ",name,"AND MY AGE IS",age)
# # name="AmAL"
# # age=22
# detaila("amal",22)
# detaila("asil",'27')

# def my_function(**kid):
#   print("His last name is ",kid)

# my_function(fname = "Tobias", lname = "Refsnes")


# def age(a):
#     if 0<=a<=18:
#         return 'baby'
#     elif 19<=a<=30:
#         return 'adult'
#     else:
#         return 'ok'
# a=age(4)
# print(a)

# a=int(input("enter a number:"))
# b=int(input("enter a number:"))
# def sum(a,b):
#     total=a+b
#     print(total)


# sum(a,b)
# print(total)


# def sum(a,b):
#     total=a+b
#     return total

# a=int(input("enter a number:"))
# b=int(input("enter a number:"))
# # print(sum(a,b))
# z=sum(a,b)
# print(z)
# print(z+20)

# def age(a,b):
    # pass

# def age(a,b):
#     print("age is",a,b)
# age(b=10,a=20)


# def sumlist(a):
#     sum=0
#     for i in a:
#         sum+=i
#     return sum
# a=[1,2,3,4,5]
# z=sumlist(a)
# print(z)

# c=z+20
# print(c)


# radius=float(input("enter radius:"))
# def aream(radius):
#     area=3.14*radius*radius
#     return area

# a=aream(radius)
# print(a)


# def valu(a):
#     a=[]
#     valu=list(input("Each element:"))
#     for i in a:
#         i+=i
#     return valu
# a=[]
# z=valu(a)
# print(z)


# factoril
def fact(n):
    fact=1
    for i in range(n):
        fact=fact*n
        n-=1
    return fact
n=int(input("Enter ur numb: "))
x=fact(n)
print(x)


