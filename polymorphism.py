# class A:
#     def findsum(self,a,b):
#         print(a+b)

#     def findsum(self,a,b,c):
#         print(a+b+c)
# obj=A()
# # obj.findsum(2,3)
# obj.findsum(2,3,4)      
#here method overloading is there which is not possible in this method of python#


#we can do the method overloading by the following method

# class A:
#     def findsum(self,a,b,c=0):
#         if c==0:
#             print(a+b)
#         else:
#             print(a+b+c)
# obj=A()
# obj.findsum(2,3,8)
# obj.findsum(2,4)


# class A:
#     def find_sum(self,a,b,c=0,d=0):
#         print(a+b+c+d)
# obj=A()
# obj.find_sum(1,2,3,4)

# class A:
#     def findsum(self,*args):
#         total=0
#         for i in args:
#             total+=i
#         print(total)
# obj=A()
# obj.findsum(2,3)
# obj.findsum(3,4,5)
# obj.findsum(1,3,3,2)



# operator overloading
# class A:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
    
# obj1=A('daniel',67)
# obj2=A('manial',80)
# print(obj1+obj2)

# so its not possible in this metod

# we can do this using an inbuilt magical function in python


class A:
    def func1(self):
        print("function 1 woorking")

    def func(self):
        print("function woorking from class A")


class C:
    def func(self):
        print("function woorking from class C")
        

class B(C,A):
    def func3(self):
        print("function 3 woorking")

    def func(self):
        print("function working from class B")
        A.func(self)
        C.func(self)#child method comes then parent method hide
        # super().func()#this methos is used when only one class inherited
obj = B() 
obj.func1()
obj.func3()
obj.func()


