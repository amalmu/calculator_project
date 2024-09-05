# import time
# class GreetingHello():
#     def hello(self):
#         for i in range(5):
#             print("hello")
#             time.sleep(1)
    
# class GreetingHi():
#     def hi(self):
#         for i in range(5):
#             print("hi")
#             time.sleep(1)
        
# start=time.time()
# objhello=GreetingHello()
# objhi=GreetingHi()
# objhello.hello()
# objhi.hi()
# end=time.time()
# print("Total time=:",end-start)

##In this case here single threading is happenig as the processor takes some time time for idle state. we can change it by 
# removing GIL(global iterate lock) by using multithreading


# import time
# from threading import Thread
# class GreetingHello(Thread):
#     def run(self):
#         for i in range(5):
#             print("hello")
#             time.sleep(1)
    
# class GreetingHi(Thread):
#     def run(self):
#         for i in range(5):
#             print("hi")
#             time.sleep(1)
        
# start=time.time()
# objhello=GreetingHello()
# objhi=GreetingHi()
# objhello.start()
# objhi.start()
# objhello.join()
# objhi.join()
# end=time.time()
# print("Total time=:",end-s



