#to print square pattern
"""n=5
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()"""

#to print right angle triangle pattern
"""n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()"""

#inverted right angle triangle pattern
"""n=5
for i in range(n):
    for j in range(n-i):
        print("*", end =" ")
    print()"""

#to print diamond pattern
#first how many rows,then how many spaces,then stars
"""n=5
for i in range(n):#i=0
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()
for i in range(n-2,-1,-1):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()"""

#armstrong number
"""a=int(input("Enter a num:"))
sum=0
temp=a
digits=len(str(a))
while temp>0:
    digit=temp%10
    sum+=digit**digits
    temp//=10
if a==sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")"""

#to print Hollow square pattern
"""n=5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()"""

#pascals patterns
"""
            1
        1       1
    1       2       1
  1     3       3      1
1    4      6      4      1
"""
# n=5
# for i in range(n):
#     print(" ",n-i-1,end=" ")