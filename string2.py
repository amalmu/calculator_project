# 1)Python program to convert lower letter to upper and upper letter to lower in a string.
# using loop

# a="AmAl"
# out=" "
# for i in a:
#     if i.isupper():
#         # print(i.lower())
#         out+=i.lower()
#     elif i.islower():
#         # print(i.upper())
#         out+=i.upper()
# print(out)
#the comment method is also possible as if we remove out+=i.lower() 
#  by out+=1 and also remove the last output statement




# Write a python program to sort letters of word by lower to upper case format.

# a="aMAlMhd"
# lower=""
# upper=""
# for i in a:
#     if i.islower():
#         # print(i.lower())
#         lower+=i.lower()
#     elif i.isupper():
#         # print(i.upper())
#         upper+=i.upper()
# print(lower+upper)


# count of given letter of word

# a=input("ENTER THE WORD: ")
# b=input("ENTER THE LETTER TO BE COUNTED")

# count=0
# for i in a:
#     if i==b:
#         count+=1
# print(count)


# a=input("ENTER 1st STRING: ")
# b=input("ENTER 2nd STRING: ")
# result=""
# lena=len(a)
# lenb=len(b)
# maxlen=max(lena,lenb)
# for i in range(maxlen):
#     if i<lena:
#         result+=a[i]
#     if i<lenb:
#         result+=b[-i-1]
# print("RESULT IS ",result)

# a=input("ENTER A STRING: ")
# s=len(a)
# string=""
# if s>=2:
#     string= a[:2]+a[-2:]
# else:
#     string="empty"
# print(string)

# a = "i am happy today gg"
# word = ""
# result = ""


# for i in range(len(a)):
#     if a[i] == ' ':
#         if len(word) % 2 == 0 and len(word) > 0:
#             result += word + ' '
#      word = ""
#     else:
#         word += a[i]
# if len(word) % 2 == 0 and len(word) > 0:
#     result += word

# print(result)  


# a = "i am happy"
# reversed_string = ""
# current_word = ""

# for i in range(len(a)):#10-0-9 i=0
#     if a[i] == ' ':#a[0]==''
#         reversed_string = current_word + ' ' + reversed_string# am + i
#         current_word = ""  
#     else:
#         current_word += a[i]#a[0] i am happy

# reversed_string = current_word + ' ' + reversed_string #happy + am i

# # reversed_string = reversed_string
# print('Reversed string:', reversed_string)


# a="iam happy cool"
# s=len(a)
# if len(a)%2==0:


# count length of string without couting the whitespace

# a="india is my country"
# length=0
# for i in a:
#     if i!=" ":
#         length+=1
# print(length)


# a = "i am happy today gg"
# words = a.split()  # Split the string into words
# result = []

# for word in words:
#     if len(word) % 2 == 0:  # Check if the word length is even
#         result.append(word)  # Add the word to the result list

# result_string = ' '.join(result)  # Join the list of words into a single string
# print(result_string)



# longest word using inbuilt

# a="Iam good"
# b=a.split(' ')
# result=b[0]
# # print(b)
# for i in b:
#     if len(i)>len(result):
#         result=i
# print(result)


# a="ms hap im ed"
# str=a.split(' ')
# word=""
# for i in str:
#     if len(i)%2==0:
#         word=i
#         print(word)

# a="9867"
# if len(a)==3:
#     print(a,"IS 3 DIGIT")
# else:
#     print("NOT 3 digit")


# def is_three_digit_number(num):
#     # Check if the number is between 100 and 999 (inclusive)
#     if num // 100 >= 1 and num // 100 <= 9 and num % 1000 == num:
#         return True
#     else:
#         return False

# # Get input from the user
# try:
#     user_input = int(input("Enter a number: "))
#     if is_three_digit_number(user_input):
#         print(f"{user_input} is a three-digit number.")
#     else:
#         print(f"{user_input} is not a three-digit number.")
# except ValueError:
#     print("Invalid input! Please enter an integer.")


a=float(input("ENTER A NUMBER:"))
value=0
if a>=100 and a<=999:
    print("ITS A 3 DIGIT:")
else:
    print("ITS NOT A 3 DIGIT:")
    


