# Count str
'''
def count_str(string):
    d={}
    for i in string.split():
        if i not in d.keys():
            d[i]=0
        d[i]+=1
    print(d)
string=input("Enter String: ")
count_str(string)
'''

# count letter
"""
def count_letter(letter):
    d={}
    for i in letter:
        if i.isalpha():
            if i not in d.keys():
                d[i]=0
            d[i]+=1
    print(d)
letter=input("Enter letter: ")
count_letter(letter)
"""

def count_vowels(word):
    vowels = "aeiouAEIOU"
    d = {}

    for i in word:
        if i in vowels:
            if i not in d.keys():
                d[i] = 0
            d[i] += 1
    print(d)

word = input("Enter a word: ")
count_vowels(word)

