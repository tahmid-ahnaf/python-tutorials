# string, integer, float, lists, dictionaries, arrays
from operator import truediv

x = "hello world"  #string
y = 3 #integer
z= 3.5 #float
a = ["apple", "mango", "jack fruit"]  #list
p ={
    "name" : "ahnaf",
    "age" : 25
} #dictionaries

# print(type(x))
# print(type(y))
# print(type(z))
# print(type(a))
# print(type(p))
# print(a)


#conditions

# a = 300
# b= 251

# print(b%2)

#even 2,4,6, ....... odd 3,5,7,.....


# if-else
# if b>a :
#     print("you can buy")
# else :
#     print("you can;t")


# nested if else
# if b>a :
#     print("you can buy")
# else :
#     if b%2 ==0:
#         print("you can't")
#     else :
#         print("manage even money")


# if condition :
#     dfadgedgdg
# else :
#     sfseegr

# take two numbers a and b , if b is greater than a then print x, else if a is equal to b then print y

# a = int(input("Enter value for a : "))
# b = int(input("Enter value for b: "))

# print(type(a))
# print(type(b))
#
# print(a/b)
# print(a//b)
#
# print (a**3)

# a = a+1000 is equivalent to a +=1000
# a+=1000
# print(a)

#if-elif-else
# if b>a:
#     print("x")
# elif a == b:
#     print("y")
# else:
#     print("z")


# take a year as input from user, print if it is leap year or not

# either this is true ----> year is divisible by 4 and not divisible by 100
# or this is true -----> year is divisible by 400

#fstrings in python

# operators +,-,/,%,**, //, +=, =, ==, -=, *=, /=, %=, //=, **=, ==, !=, >, <,>=, <=, and, or , not


#leap year check

year = int(input("Give a year to check if it is leap year or not: "))

if  (year%4 == 0 and year%100 != 0) or (year%400 ==0) :
    print(f"{year} is a leap year")
else :
    print(f"{year} is not leap year")

# q = 6
#
# print(q==5)

# m = True
# n = False
#
# print(m or n)

# m or n can only be false when m and n both are false, if any of them is true, then m or n is true
# m and n can only be true when m and n both are true, if any of them is false, then m and n is false











