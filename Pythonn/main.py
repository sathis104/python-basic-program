#armstrong
'''
for num in range(1001):
    temp=num
    result= 0
    n=len(str(num))
    while(num!=0):
        arm=num%10
        result=result+arm**n
        num=num//10
    if(temp==result):
        print(temp)
'''
#pattern
'''
n=int(input("Enter No:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("|"+ str(i),end="|")
    print("")
'''
#star
'''
n=int(input("Enter No:"))
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1 or i==j:
            print("*",end="")
        else:
            print(end=" ")
    print()
'''
#factorial
'''
n=int(input("Enter No:"))
fact=1
for i in range(n,0,-1):
    fact=fact*i
print(fact)
'''

#Star
'''
n=int(input("Enter No:"))
for i in range(n):
    for j in range(n):
        if j==4 or i==j or i==0:
            print("* ",end="")
        else:
            print(end="  ")
    print()
'''


'''
n=int(input("Enter No:"))
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num=num+1
    print("")

1 
2 3 
4 5 6 
7 8 9 10 
'''

#python pattern
'''
str = input("Enter str:")
len=len(str)
for i in range(len):
    for j in range(i+1):
        print(str[j],end="")
    print("")
    
p
py
pyt
pyth
pytho
python

'''

#Fibnocci series
'''
n=int(input("Enter Range:"))
a=0
b=1
print(a, b)
for i in range(n+1):
    c=a+b
    print(c)
    a=b
    b=c
'''

'''
n=int(input("Enter No:"))
num=1
for i in range(n+1,0,-1):
    for j in range(1,i+1):
        print(num,end=" ")
        num=num+1
    print("")
    num=1

1 2 3 4 5 6 
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
'''
'''
n=int(input("Enter No:"))
num=1
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(num,end=" ")
    print("")
    num = num + 1
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5 
'''


