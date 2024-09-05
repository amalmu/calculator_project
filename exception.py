# try:
#     print(10/0)
# except:
#     print("ITS ZERO")


# try:
#     x=int(input("Enter numb: "))
#     print(x>9)
# except:
#     print("WRONG")


# try:
#     x = int(input("Enter number: "))
#     print(x > 9)
# except ValueError:
#     print("WRONG")


# try:
#     print(10)
# except:
#     print("MANDAN")
# else:
#     print("GET LOST")
# finally:
#     print("GOOD LUCK")

# try:
#     print(x)
# except NameError as n:
#     print("WOW GREAT EFFORT",n)

#factorial using exception

# try:
#     n=int(input("enter numb: "))
#     fact=1
#     if n>0:
#         for i in range(1,n+1):
#             fact*=i
#             # i-=1
#         print(fact)
#     elif n<0:
#         raise NameError
# except:
#     print("wrong")

# try:
#     class Fact:
#         def __init__(self,n,fact=1):
#             self.n=n
#             self.fact=fact
            
#         def show(self):
            
#             if n>=0:
#                 for i in range(1,self.n+1):
#                     self.fact*=i
#                     i-=1
#                 print(self.fact)
#             elif self.n<0:
#                 raise NameError("HIHI")
# except:
#     print("wrong")
# n=int(input("enter numb: "))

# ob=Fact(n)
# ob.show()


# try:
#     class Fact:
#         def __init__(self, n, fact=1):
#             self.n = n
#             self.fact = fact
            
#         def show(self):
#             if self.n >= 0:
#                 for i in range(1, self.n + 1):
#                     self.fact *= i
#                 print(self.fact)
#             elif self.n < 0:
#                 raise ValueError("n should be a non-negative integer.")
# except ValueError as ve:
#     print(ve)
# except Exception as e:
#     print("An error occurred:", e)

# n = int(input("Enter number: "))

# ob = Fact(n)
# ob.show()



# class Fact:
#     def __init__(self, n, fact=1):
#         self.n = n
#         self.fact = fact
        
#     def show(self):
#         if self.n >= 0:
#             for i in range(1, self.n + 1):
#                 self.fact *= i
#             print(self.fact)
#         elif self.n < 0:
#             raise ValueError("n should be a non-negative integer.")

# try:
    
#     ob = Fact(n = int(input("Enter number: ")))
#     ob.show()
# except ValueError as ve:
#     print(ve)
# except Exception as e:
#     print("An error occurred:", e)


