""" dict1={
    'name':'john','age':'25','city':'mumbai','course':'computer'
}
print(dict1)
print(dict1['name'])
print(dict1['course'])
dict1['email']="amit@gmail.com"
print(dict1)

dict1["age"]=21
print(dict1)

dict1.pop("course")
print(dict1)

print(len(dict1))

if "salary" in dict1:
    print("salary exists")
else:
    print("salary not exists")

print(dict1.keys())

print(dict1.values())

for key,value  in dict1.items():
    print(key,":",value) """



""" numbers=[10,20,10,30,20,10]
freq={}
for i in numbers:
    freq[i]=numbers.count(i)
print(freq) """

""" student={
    "bharat":78,
    "shreya":89,
    "shruti":45,
    "om":98,
    "yuvaraj":14
    }
highest=max(student,key=student.get)
lowest=min(student,key=student.get)
print("highest:-",student[highest])
print("lowest:-",student[lowest])


print(sum(student.values()))

dict1.update(student)
print(dict1)

 """
""" square={}
for i in range(1,11):
    square[i]=i*i
print(square)


 """

""" numbers="bharat"
freq={}
for i in numbers:
    freq[i]=numbers.count(i)
print(freq) """



""" student={
    "bharat":78,
    "shreya":89,
    "shruti":45,
    "om":98,
    "yuvaraj":14
    }
swap={}
for key,value  in student.items():
    swap[value]=key
print(swap) """

""" #nested dictonary
student={"1":"rohit", "2":{"a":"python","b":"css"}}
print(student) 

 """

""" numbers=input("enter a sentence: ")
freq={}
for i in numbers:
    freq[i]=numbers.count(i)
print(freq) """


""" products={
    "biscuit":1,
    "chips":5,
    "chocklet":8,
    "juce":6
}
print(products)
products["mango"]="7"
print(products)
products["chips"]="2"
print(products)
print(products.pop("chips"))
print(products)
 """

""" grades={
    "99":"a",
    "87":"b",
    "75":"c",
    "64":"d",
    "54":"e",
    "35":"fail"
}
print("graades =",grades)
for key in sorted(grades):
     """







