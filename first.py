# print("amal")
# print("hello")
# a=10
# a=20
# a=30
# print(a)
# a=("vishnu123")
# print(a)

# print(10+20)


# print(10-20)
# print(10*20)

# print(10/20)

# a=10
# b=20
# c=a+b
# print(c)


# d=c+70
# print(d)

# print(c+d)

# print(c+b)

# a='vishnu'
# print(a)


# a=input('enter ur name:')
# print(a)

# a=int(input("enter first numb:"))
# b=int(input('enter ur 2nd numb:'))
# c=a-b
# print(c)


# a=10
# A=10
# print(A)

# amal12355=10
# print('amal12355')

# _amal=10
# print(_amal)

# print(type(_amal))

# n=float(input("enter a numb:"))
# print(n)


# n=3
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
#     i-=1
# print(fact)

try:
    n = int(input("Enter a positive integer: "))
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    fact = 1
    for i in range(1, n + 1):
        fact *= i

    print(f"The factorial of {n} is {fact}")

except ValueError as ve:
    print(f"Error: {ve}")
except TypeError:
    print("Error: The input must be an integer.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
