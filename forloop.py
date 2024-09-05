#BASIC QUESTIPONS

# for i in range(1,9):
#     print (i)


# for i in range(2,11,3):
#     print(i)

# for i in range(1,10):
#     if i==4:
#         break
#     print(i)

# for i in range(2,7):
#     if i==5:
#         continue
#     print(i)

# for i in range(98,23,-3):
#     print(i)

# for i in range(10):
#     if i==3:
#         print(i)
# else:
#     print("MUMMY")


# for i in range(1,10):
#     if i%2==0:
#         print("even numberare",i)
#     else:
#         print("odd numbers are",i)

#SUM OF FIRST 10 NATURAL NUMBERS

# sum=0
# for i in range(0,11):
#    sum=sum+i
# print(sum)

# for i in range(1,21):
#     if i%2==0:
#         print(i)


#COUNT OF VOWELS
# a=str(input("ENTER A STRING: "))
# vowel="aeiouAEIOU"
# count=0
# for i in a:
#     if i in vowel:
#         count+=1
# print(count)

# # FACTORIAL 
# num = int(input("ENTER A NUMBER: "))
# fact = 1
# for i in range(1, num + 1):
#     fact *= i
# print("FACTORIAL IS", fact)

#REVERSE A number

# num=int(input("ENTER A NUMBER: "))
# rev=0
# length=len(str(num))
# for i in range(length):
#     x=num%10
#     rev=rev*10+x
#     num=num//10
# print("THE REVERSE =",rev)