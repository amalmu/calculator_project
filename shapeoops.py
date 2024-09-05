class Shape:
    def __init__(self):
         pass
        
class Circle(Shape):
        
        def __init__(self,r):
            # Shape.__init__(self,area,per)
            self.r=r
        def area(self):
            #  Shape.__init__(self)
             area=3.14*self.r*self.r
             return area
        def per(self):
              per=2*3.14*self.r
              return per
class Square(Shape):
        def __init__(self,side):
            self.side=side
        def area(self):
             area=self.side*self.side
             return area
        def per(self):
             per=self.side*4
             return per
print("choice1=circle")
print('choice2=square')

choice=int(input("enter ur choice="))



if choice==1:
    # obj=Circle(int(input("enter radius:")))  #another method
    r=int(input("enter rad:"))
    obj=Circle(r)
    print("area.circle=",obj.area())
    print("perimetr.circle=",obj.per())

elif choice==2:
    kl=Square(int(input("enter side:"))) #another method
    side=int(input("enter sid"))
    kl=Square(side)
    print("area.square=",kl.area())
    print("per.square=",kl.per())
else:
     print("INVALID")