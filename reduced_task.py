""" #1
from functools import reduce 
a=[10,20,30,40,50]
sum=reduce(lambda x,y:x+y,a)
print(sum)
 """


""" #2
from functools import reduce
a=[25,80,15,100,45]
maxium=reduce(lambda x,y: x if x>y else y,a)
print("maxium number:-",maxium) """


""" #3
from functools import reduce
a=[1,2,3,4,5]
multiplication=reduce(lambda x,y:x*y,a)
print("multiplication=",multiplication) """


""" #4
from functools import reduce
string=["python","is","awesome"]
concat=reduce(lambda x,y: x+y,string)
print("concatinate string:-",concat)

 """

""" #5
from functools import reduce
salary={"sagar":50000, "bharat":60000, "guddu":4000, "shruti":30000,"shreya":100000}
total=reduce(lambda x,y: x+y,salary.values())
print(total) """