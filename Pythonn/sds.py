#Prime 1
'''
n1 = int(input("Enter No:"))
n2 = int(input("Enter No:"))

for num in range(n1,n2+1):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)
#prime 2
n = int(input("Enter No:"))
count = 0

for i in range(2, n):
    if n % i == 0:
        count = count + 1

if count == 0:
    print("Prime")
else:
    print("Not Prime")
'''

#perfect Number
'''
n = int(input("Enter No:"))
perfect=0
for i in range(1,n):
    if(n%i==0):
        perfect=perfect+i
if(perfect==n):
    print("Perfect")
else:
    print("Not")

2nd method

low = int(input("Enter No:"))
high = int(input("Enter No:"))

for num in range(low, high + 1):
    perfect = 0
    for i in range(1, num):
        if num % i == 0:
            perfect += i
    if num == perfect:
        print(num)

'''

#Star using while
'''
n = int(input("Enter No:"))
row=0
while(row<n):
    star =row+1
    while(star>0):
        print("*",end="")
        star=star-1
    row=row+1
    print("")
'''

'''
def reverse(n):
    rev_str=""
    for i in n:
        rev_str=i+rev_str
    print(rev_str)


n = input("Enter String:")
reverse(n)
'''


#Star

'''
n = int(input("Enter No:"))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(format(" ", "<3") ,end="")
    for j in range(i,0,-1):
        print(format(j,"<3"),end="")
    for j in range(2,i+1):
        print(format(j,"<3"),end="")
    print("")
    
            1  
         2  1  2  
      3  2  1  2  3  
   4  3  2  1  2  3  4  
5  4  3  2  1  2  3  4  5  
'''
#minimum
'''
ls=[10,85,5,6,91,4]
min=ls[0]
for i in range(1,len(ls)):
    if ls[i]<min:
        min=ls[i]
print(min)
'''

n=input("Enter:")
str=""
for i in n:
    str=i+str
print(str)
