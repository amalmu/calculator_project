class Employee:
    class Company:
        def __init__(self,name,loc,spec):
            self.name=name
            self.loc=loc
            self.spec=spec
    def __init__(self,empname,id,cname,cloc,cspec):
        self.empname=empname
        self.id=id
        self.comp=Employee.Company(cname,cloc,cspec)
    def show(self):
        
        print('cname=',self.comp.name)
        print("cloc=",self.comp.loc)
        print("cpec=",self.comp.spec)
        print('empname=',self.empname)
        print('empid=',self.id)
       
sw=Employee("amal",18643,'yen','manlore','degree')
sw.show()




#         # multiple inheritance

# class Father:
#     fname=" "
    
#     def pr(self):
#         print(self.fname)
# class Mother:
#     mname=" "
    
#     def cr(self):
#         print(self.mname)
# class Son(Father,Mother):
#     def parents(self):
#         print("fathrmother=",self.fname+self.mname)
        
# sq=Son()
# sq.fname="Abi"
# sq.mname="Rani"
# sq.pr()
# sq.cr()
# sq.parents()
# \
    
class Vehicle:
    def __init__(self,company,model,color,engine,fuel):
        self.company=company
        self.model=model
        self.color=color
        self.engine=engine
        self.fuel=fuel
    def start_engine(self):
        print("starting engine")

    def change_gear(self):
        print("changing gear")
        # print("company",self.company)

class Car(Vehicle):
    def open_door(self):
        print("opening door")
        print(self.company)

c=Car("bmw","m5","black",3000,"petrol")
c.start_engine()
c.change_gear()
c.open_door()