""" a="i am bharat i am"
print(a)
print("number of am present  =",a.count("am"))

 """

""" #find the longest word in a sentence)
sentence=input("enter a sentence:-")
words=sentence.split()
longest=""
for i in  words:
    if len(i)>len(longest):
        longest=i
print("longest word=",longest) """


""" str1=input("enter a first string")
str2=input("enter a second string") # listen.silent
if(sorted(str1)==sorted(str2)):
    print("string are anagram ")
else:
    print("string are not anagram")

 """



""" text = input("Enter a string: ")
result = ""
for ch in text:
    if ch.isalnum():
        result += ch
print("String after removing special characters =", result)

 """


""" # Count uppercase letters, lowercase letters, digits, and special characters
text = input("Enter a string: ")
upper = 0
lower = 0
digit = 0
special = 0
for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    else:
        special += 1
print("Uppercase Letters =", upper)
print("Lowercase Letters =", lower)
print("Digits =", digit)
print("Special Characters =", special) """



""" n="python programming tutorial"
print(n.title())
 """


""" name=input("enter a string:-")
print("afterv swapping:-",name.swapcase())
"""


""" abc=input("enter a string:-")
result=""
for i in abc:
    if i not in result:
        result+=i
print("string after no duplicates:-",result) """



""" b="bharat"
print("is this string contain only aplhabets:-",b.isalpha())
 """


""" text = input("Enter a string: ")
for i in range(len(text)):
    for j in range(i + 1, len(text) + 1):
        print(text[i:j])       
 """







