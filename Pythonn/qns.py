# Write code to check if a String is palindrome or not?
'''
str = input("Enter String: ")
print("org_String: ", str)
str_rev = ""
for i in range(len(str)):
    str_rev = str[i] + str_rev
print("reversed String: ", str_rev)
if(str_rev==str):
    print("palindrome")
else:
    print("Not")
'''

# Write a method which will remove any given character from a String?
'''
str = "hello ,world"
new_str = ""
for i in str:
    if i!=',':
        new_str+=i
print(new_str)
'''

# How to count the occurrence of a given character in a String?
'''
def count_char(letter):
    d={}
    for i in letter:
        if i.isalpha():
            if i not in d.keys():
                d[i]= 0
            d[i] = d[i]+1
    print(d)
letter =input("Enter letter: ")
count_char(letter)
'''

#  Write a program to find the longest word in a given sentence.
'''
def long_word(string):
    l = 0
    w = ""
    words = string.split()
    for i in words:
        if len(i) > l:
            w = i
            l = len(i)
    print(w, l)


string = input("Enter : ")
long_word(string)
'''

# How can you reverse a string?
'''
str = input("Enter String: ")
print("org_String: ", str)
str_rev = ""
for i in range(len(str)):
    str_rev = str[i] + str_rev
print("reversed String: ", str_rev)
'''

# How do you reverse words in a given sentence without using any library method?
# same code


# How to calculate the number of vowels and consonants in a string?

'''
def count(string):
    vowels = 0
    consonant = 0
    given = "AEIOUaeiou"
    for i in string:
        if i in given:
            vowels += 1
        else:
            consonant += 1
    print(vowels, consonant)


string = input("enter :")
count(string)
'''

# In an array 1-100 multiple numbers are duplicates, how do you find it?
'''
def count_duplicate(numbers):
    duplicate = []
    for i in numbers:
        if numbers.count(i) > 1:
            if i not in duplicate:
                duplicate.append(i)
    print(duplicate)

numbers = [1, 2, 3, 5, 4, 7, 8, 9, 4, 5, 1, 41, 52, 78, 96, 45, 78, 12, 3, 52, 56, 45, 12,
           12]
count_duplicate(numbers)
'''
# Given two arrays, 1,2,3,4,5 and 2,3,1,0,5 find which number is not present in the second array.
'''
a = [1, 2, 3, 4, 5]
b = [2, 3, 1, 0, 5]

set_a = set(a)
set_b = set(b)

diff = set_a.difference(set_b)
print(diff)

for i in a:
    if i not in b:
        print(i)
'''
# Write a program to reverse the array
'''
a = [1, 2, 3, 4, 5]
st = 0
en = len(a) - 1
while st < en:
    temp = a[st]
    a[st] = a[en]
    a[en] = temp
    st += 1
    en -= 1
print(a)
'''

# Write a program to sort the given array

'''
a = [5, 1, 2, 3, 4, 8, 7, 6, 0, 9, 10]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(a)
'''

# How to find the largest and smallest number in an array?
'''
a = [5, 1, 2, 3, 4, 8, 7, 6, 0, -9, 10]
min=a[0]
for i in range(1,len(a)):
    if a[i]<min:
        min=a[i]
print(min)
'''
# Write a program to check whether a number is a palindrome or not?
'''
n= int(input("Enter"))
print("Original Number",n)
temp=n
rev=0
while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("Reversed Number",rev)
if temp==rev:
    print("palindrome")
else:
    print("Not Palnindrome")
'''
# Write code to check whether an integer is an Armstrong number or not?
'''
n= int(input("Enter"))
temp=n
le=len(str(n))
res=0
while(n!=0):
    arm=n%10
    res=res+arm**le
    n=n//10
if(temp==res):
    print("Armtrong")
else:
    print("Not ")
'''
# How to find the sum of digits of a number?
'''
n=int(input("enter"))
perfect=0
for i in range(1,n):
    if n%i==0:
        perfect=perfect+i
print(perfect)
'''


# additional
# How to remove a number without in-built function?
'''
a=[1, 2, 3, 5, 4, 7, 8, 9, 4, 5, 1, 41]
b=[]
for i in a:
    if i!=9:
        b.append(i)
print(b)
'''
a=[1, 2, 3, 5, 4, 7, 8, 9, 4, 5, 1, 41]
a.remove(9)
print(a)







