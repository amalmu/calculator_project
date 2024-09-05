# inner class
# class Salim:
#     class Amal:
#         def __init__(self,name,father,mother):
#             self.name=name
#             self.father=father
#             self.mother=mother
#     def __init__(self,name,father,mother,cname,cfather,cmother):
#         self.name=name
#         self.father=father
#         self.mother=mother
#         self.company=Salim.Amal(cname,cfather,cmother)
    
#     def show(self):
#         print(self.company.name,self.company.father,self.company.mother)
#         print(self.name,self.father,self.mother)

# ob=Salim('salim','shahulhammed','ummal','amal','sal','rajeena')
# ob.show()


# study inherigance

class Operation:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print('add=',self.a+self.b)
    def sub(self):
        print('sub=',self.a-self.b)
    def mul(self):
        print('mul=',self.a*self.b)
    def div(self):
        print('div=',self.a/self.b)
print("CHOICE")
print("1=add",'2=sub','3=mul','4=div')
choice=int(input("enter your choice: "))
a=int(input("enter a: "))
b=int(input("enter b: "))
ob=Operation(a,b)

if choice==1:
    ob.add()
elif choice==2:
    ob.sub()
elif choice==3:
    ob.mul()
elif choice==4:
    if b!=0:
        ob.div()
    else:
        print("DINOMINATOR 0")

else:
    print("INVALID")

    
    