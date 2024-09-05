# class School:
#     def __init__(self,name,age,ph):
#         self.name=name
#         self.age=age
#         self.ph=ph
#     def va(self):
#         print(self.name,self.age,self.ph)
# per1=School("Amal",22,9987665437)
# per1.va()


# class Circle:
#     def __init__(self,radius):
#         self.r=radius
    
#     def area(self):
#         return 3.14*self.r*self.r
    
# radius=int(input("Enter the radius: "))  
# c1=Circle(radius)
# print(c1.area())


# class Calculator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
    
#     def add(self):
#          return self.a+self.b
#     def sub(self):
#         return self.a-self.b
#     def multi(self):
#         return self.a*self.b
#     def div(self):
#         return self.a/self.b
        
# print("ENTER THE CHOICE=1,2,3,4")
# choice=int(input("Enter choice: "))
# a=int(input("Enter the first number: "))
# b=int(input("Enter the 2nd number: "))
# cal1=Calculator(a,b)

# if choice==1:
#       print("The sum is",cal1.add())
# elif choice==2:
#       print("The difference is",cal1.sub())
# elif choice==3:
#       print("The product is",cal1.multi())
# elif choice==4 and b!=0:
#       print("The answer is",cal1.div())
# else:
#       print("Invalid choice")


# class Student:
#     school="Detan School"
#     def __init__(self,name,age,std,div):
#         self.name=name
#         self.age=age
#         self.std=std
#         self.div=div
#     def details(self):
#         print('name: ',self.name)
#         print('age: ',self.age)
#         print('std: ',self.std)
#         print('div: ',self.div)
#         # or in place of sabraigiri school
#         # print("school=",Student.school) #that is school=detan school
#     def marks(self,physics,maths,chemistry):
#         self.physics=physics
#         self.maths=maths
#         self.chemistry=chemistry
#     def display(self):
#         print("physics= ",self.physics)
#         print("maths= ",self.maths)
#         print("chemistry= ",self.chemistry)
#         print("Total marks= ",self.physics+self.maths+self.chemistry)
# name=input("enter your name: ")
# age=int(input("enter your age: "))
# std=int(input("enter ur std: "))
# div=input("enter your division: ")
# physics=int(input("enter your marks,physics: "))
# maths=int(input("enter your marks,maths: "))
# chemistry=int(input("enter your marks,chemistry: "))
# print("Sabarigiri School")
# cd=Student(name,age,std,div)
# cd.details()
# cd.marks(physics,maths,chemistry)
# cd.display()



