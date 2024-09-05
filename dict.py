# dict={
#     'name':'amal',
#     'age':20,
#     'place':'tvm'

# }

# print(dict['name'])
# print(len(dict))
# print(dict.keys())
# print(dict.values())
# print(dict.items())

# nested dict

# college={
#     'student1':{
#         'name':'amal','place':'tvm'
#         },
#     'student2':{
#         'name':'adil','place':'kollm'
#         }
# }
# print(college)
# print(college['student1']['place'])

# n1=int(input("ENTER 1ST NUMBER: "))
# n2=int(input("ENTER 2ND NUMBER: "))
# operation=int(input('ENTER THE OPEARTION: '))
# output=0
# if operation==1:
#     output=n1+n2
# elif operation==2:
#     output=n1-n2
# elif operation==3:
#     output=n1*n2
# elif operation==4:
#     output=n1/n2
# else:
#     print("NOT")
    
# print(output)





while True:
    op=int(input("OPRTION: "))
    
    if op==5:
        break
    n1=int(input("ENTER !ST: "))
    n2=int(input("ENTER 2nd: "))
    if op==1:
        add=n1+n2
        print(add)

    elif op==2:
        sub=n1-n2
        print(sub)

    elif op==3:
        mul=n1*n2
        print(mul)

    elif op==4:
        div=n1/n2
        print(div)

    else:
        print("INVALID")




# a=[234,45]
# print(a)
# b=a.index(45)
# print(b)

# a[b]=99
# print(a)

# phb={'amal':{
#     'name':'amal',
#     'email':'amalmhd@gmail.com',
#     'phno':[78789,89898]
#     },
#     'farhan':{
#         'name':'farhan',
#         'email':'farhan@gmail.com',
#         'phno':[56565,65767]
#     }}

# name_update=input("ENter name to update: ")
# phn_update=int(input("Enter phno to update: "))
# new_no=int(input("Enter new number: "))
# z=phb[name_update]['phno']
# k=z.index(phn_update)
# z[k]=new_no
# # phb[name_update]['phno']=z
# print(phb)


# phonebook to update all details

pb={}
while True:
    print('''
          1.add values,
          2.view,
          3.update name,
          4.update email,
          5.update phno,
          6.delete details,
          7.exit'''
 )

    choice=int(input("enter your choice: "))
    if choice==1:
        sub={}
        name=input("enter your name:")
        email=input("enter your email:")
        c=int(input("E NTER COUNT OF PHONE NO:"))
        l=[]
        for i in range(c):
            ph=int(input("enter your numbers:"))
            l.append(ph)
            # sub['c']=l
        sub['name']=name
        sub['email']=email
        sub['phone']=l
        pb[name]=sub
    elif choice==2:
        print(pb)
    elif choice==3:
        print("UPDATE NAME")
        old=input("enter old name")
        if old in pb:
            new=input("ENTER new NAME: ")
            pb[new]=pb.pop(old)
            pb[new]['name']=new
        else:
            print("NOT FOUUND")
    elif choice==4:
        print("EMAIL UPDATTE")
        name=input("ENTER THE name: ")
        if name in pb:
            newemail=input("ENTE THE NEW: ")
            pb[name]['email']=newemail
        else:
            print("NOT FOUND CONTCT")
    elif choice==5:
        print("PHNO UPDATE   ")
        name=(input("ENTR THE name "))
        exist=pb[name]['phone']
        if name in pb:
            index=int(input("ENNTR THE INDEX VALUE: "))
            if 1<=index<=len(exist):
                newp=int(input("ENTR THE NEW ONE: "))
                pb[name]['phone']=newp
            else:
                print("INvalid index")
        else:
            print("NOT FOUND")
    elif choice==6:
        print("DELETE OPTION SELECTED")
        name=input("ENTER THE NAME: ")
        if name in pb:
            del pb[name]
            print('deleted')
        else:
            print('name not found')
    elif choice==7:
        break
    else:
        print("INVALID CHOICE")
print("bye")

        



 

