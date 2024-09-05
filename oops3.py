#Percentage of marks using variable as list
# class Student:
#     def __init__(self,name,age,marks:list):
#         self.name=name
#         self.age=age
#         self.marks=marks
#     def show(self):
#         print("name:",self.name)
#         print("age=",self.age)
#         print("marks=",self.marks)
#     def per(self):
#         tot=0
#         for i in self.marks:
#             tot=tot+i
#             per=(tot/400)*100
#         print("Percentage is",tot)
    

# sq=Student("Amal",20,[23,3,33])
# sq.show()
# sq.per()






# accesing obj from another class
# class Company:
#     def __init__(self,cname,loc,year):
#         self.cname=cname
#         self.loc=loc
#         self.year=year
    
# class Employee:
#     def __init__(self,empname,id,place,comp:Company):
#         self.empname=empname
#         self.id=id
#         self.place=place
#         self.comp=comp
#     def show(self):
#         print("empname=",self.empname)
#         print("id=",self.id)
#         print("place=",self.place)
#         print("compname=",self.comp.cname)
#         print("comploc=",self.comp.loc)
#         print("compyear=",self.comp.year)
# sq=Company("Yenepoya","Kowdiar",2021)
# sw=Employee("Viswas",18643,"pathady",sq)
# sw.show()



# inner class
# class Employee:
#     class Company:
#         def __init__(self,cname,loc,year):
#             self.cname=cname
#             self.loc=loc
#             self.year=year
#     def __init__(self,empname,id,place,comp:Company):
#         self.empname=empname
#         self.id=id
#         self.place=place
#         self.comp=comp
#     def show(self):
#         print("empname=",self.empname)
#         print("id=",self.id)
#         print("place=",self.place)
#         print("compname=",self.comp.cname)
#         print("comploc=",self.comp.loc)
#         print("compyear=",self.comp.year)
# sq=Employee.Company("Yenepoya","Kowdiar",2021)
# sw=Employee("Viswas",18643,"pathady",sq)
# sw.show()

# class Student:
#     school="abcd school"#class varable

#     def __init__(self,roll_no,name,study_class,class_teacher):
#         self.roll_num=roll_no
#         self.name=name
#         self.study_class=study_class
#         self.class_teacher=class_teacher

#     def display_studentdetails(self):#object/instance methods
#         print("fname",self.name)
#         print("rollnum",self.roll_num)
#         print("studyclass",self.study_class)
#         print("class_teacher",self.class_teacher)
    
    
#     def huy():
#         print("GOOD school")

# Student.huy()

# another method

