name="bharat"
print("length of string=",len(name))

print(name[0])
print(name[5])


abc="python tutorial"
if "python"in abc:
    print("python is present ")
else:
    print("python is not present")


name="bharat"
print("in uppercase=",name.upper())
print("in lowercase=",name.lower()) 


print(name[::-1]) 


text="python programming"
count=0
for i in text:
    if i in "aeiou":
        count=count+1
print("vowels=",count)
 
 
a="bharat"
c=a.count("a")
print("number of occurance of a=",c) 


