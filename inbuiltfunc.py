#  1) Given 2 strings, s1, and s2 return a new string made of the first, middle and last 
# charecters each input string
# A=abcde  B=uvwxyz   out­­­­-> aucxez

#3 Given two strings, s1 and s2, create a mixed String
# s1 = "Abc"
# s2 = "Xyz"
# AzbycX

# s1="Abc"
# s2="Xyz"
# str=" "
# for i in s1:
#     print(s1.replace("b"))

# print(s1+s2)


# QUESTION 3 date  27 june in mail
# str1 =(input("ENTER A STRING:"))
# count_lower=0
# count_upper=0
# count_digit=0
# count_symbol=0

# for i in str1:
#     if i.isupper():
#         count_upper+=1
#     elif i.islower():
#         count_lower+=1
#     elif i.isalnum():
#         count_digit+=1
#     else:
#         count_symbol+=1
# print("COUNT OF UPPERSCASE=",count_upper)
# print("LOWERCASE COUNT ",count_lower)
# print("DIGITS COUNT=",count_digit)
# print("COUNT OF SYMBOLS IS ",count_symbol)


# 0)Write a program to count the number of letters in a word. using loop

# str=input("ENTER A STRING:")
# count=0
# for i in str:
#     if i.isalpha():
#         count+=1

# print("THE COUNT IS",count)



#  Write a Python program to get a string from a given string 
# where all occurrences of its first char have been changed to '$', 
# except the first char itself. 
# Sample String : 'restart'
# Expected Result : 'resta$t'

str=input("ENTER A STRING:")
a=str[0]
new=a+str[1:].replace(a,"$")
print(new)

# question4 emma-is-a-datascientist

# a="emma-is-a-datascientist"
# spl=a.split("-")
# word=" "

# for i in spl:
#     #not neccesary = a.replace("-","  ")
#     word+=i+" "
# print(word)
    
