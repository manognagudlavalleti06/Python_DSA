# x=int(input("Enter a number:"))
# y=int(input("Enter a number:"))
# try:
#     print(x/y)
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as ve:
#     print(ve)
# finally:
#     print("done")

# for i in range(5):
#     if i==6:
#         break
#         print(i)
# else:
#     print("done")

# try:
#     a=int(input("Enter a number:"))
#     print(a)
# except ValueError as e:
#     print(e)
# else:
#     print("done")

#to throw error
# a=int(input("Enter a number:"))
# if a <0:
#     raise ValueError("Num is negative")
# else:
#     print(a)

#keep asking valid integer number if not valid integer number , print error
# while True:
#     try:
#         a=int(input("Enter a number:"))
#         print(a)
#         break
#     except ValueError as e:
#         print(e) #or
# try:
#     a=int(input("Enter Num:"))
#     if a > 0:
#         print(a)
# except ValueError as e:
#     print(e)

#handle index error while accessing list elements if it is out of range handle it
l=[1,2,3,4,5,6]
try:
    print(l[8])
except IndexError as ie:
    print(ie)
