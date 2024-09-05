# class Car:
#     def __init__(self,cname,color,year):
#         self.cname=cname
#         self.color=color
#         self.year=year
#     def sh(self):
#         print("close it")
#         print(self.color)

# class Mine(Car):
#     def __init__(self,cname,color,year,bodytype):
#         super().__init__(cname,color,year)
#         self.bodytype=bodytype
#     def fg(self):
#         print("open it")
#         print(self.color)
#         print(self.bodytype)

# ob=Mine("maruti",'yellow',2019,'hatch')
# ob.fg()
# print(ob.color)
# print(ob.bodytype)


# mutilevel inheritance


# class Grandfather:
#     def __init__(self,gname):
#         self.gname=gname


# class Father(Grandfather):
#     def __init__(self,fname,gname):
#         Grandfather.__init__(self,gname)
#         self.fname=fname
#     def f(self):
#         print("Gud boy")

# class Son(Father):
#     def __init__(self,sname,gname,fname):
#         Father.__init__(self,fname,gname)
#         self.sname=sname
    
#     def det(self):
#         print("gname=",self.gname)
#         print("fname=",self.fname)
#         print("sname=",self.sname)

# obj=Son('amal','kkkamal','kamal')
# obj.det()
# obj.f()

# class Parent:
#     def __init__(self,pname):
#         self.pname=pname
#     def show(self):
#         return self.pname
# class Child1(Parent):
#     def __init__(self,c1name):
#         self.c1name=c1name
#     def ow(self):
#         return self.c1name
# class Child2(Parent):
#     def __init__(self,c2name):
#         self.c2name=c2name
#     def ds(self):
#         return self.c2name
# ob=Child1("Amal")
# oh=Child2("Adil")
# print(ob.ow())
# print(oh.ds())


# hierarchil inheritnce


# class Parent:
#     def fun1(self):
#         print("FUNC 1")
# class Child1(Parent):
#     def fun2(self):
#         print("FUNC 2")
# class Child2(Parent):
#     def fun3(self):
#         print("FUNC 3")
# ob=Parent()
# obj1=Child1()
# obj2=Child2()
# # obj1.fun1()
# # obj2.fun3()
# # obj2.fun1()
# # obj1.fun2()
# ob.fun1()
# ob.fun2()