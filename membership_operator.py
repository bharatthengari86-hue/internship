 # check character in string
name="bharat"
print(name)
abc=input("enter character to search:-")
print(abc,"in string",abc in name)
print(abc,"not in string",abc not in name) 


#check student name in a list
student_name=["bharat","guddu","om","yuvaraj","adity"]
print(student_name)
c=input("enter student name to serach in list :-")
print(c,"in list",c in student_name)
print(c,"not in list",c not in student_name) 


#check number in tuple
tup=(35,87,9,12)
print(tup)
c=int(input("enter the number to search in tuple :-"))
print(c,"in list",c in tup)
print(c,"not in list",c not in tup)