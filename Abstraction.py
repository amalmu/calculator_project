# from abc import ABC,abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def changegear(self):
#         pass

#     def startengine(self):
#         print("start the engine")
    
# class Car(Vehicle):
#     def applbreak(self):
#         print("apply the break")
#     def changegear(self):
#         print("change the gear automatically")

# class Truck(Vehicle):
#     def opendoor(self):
#         print("open the door")
#     def changegear(self):
#         print("change the gear manually")

# c=Car()
# t=Truck()
# c.applbreak()
# c.changegear()
# t.changegear()
## print(type(Vehicle))

# from abc import ABC,abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def changegear(self):
#         pass

#     def startengine(self):
#         print("start the engine")
    
# class Car():
#     def applbreak(self):
#         print("apply the break")
#     def changegear(self):
#         print("change the gear automatically")

# class Truck(Car,Vehicle):
#     def opendoor(self):
#         print("open the door")
#     def changegear(self):
#         print("change the gear manually")
#         Car.changegear(self)


# obj=Truck()
# obj.changegear()


class Polygon:
    def shape(self):
        