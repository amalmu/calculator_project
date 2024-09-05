
a=int(input("enter a number:"))
if a<=100:
    print("the person is secured with A grade")
    if a<90:
        print("the person is secured with B grade")
    if a<80:
        print("the person is secured with C grade")
    if a<60:
        print("the person is secured with D grade")

else:
    print("the person is failed")
