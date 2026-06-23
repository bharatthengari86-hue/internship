#retun Function

""" #1
abc=[10,15,22,33,40,55,60]
print(abc)
even=list(filter(lambda a: a%2==0 ,abc))
print("even numbers=",even)
 """

""" #2
a=[-10,5,-3,8,0,15,-7]
print(a)
p=list(filter(lambda s: s>0 ,a))
print(p) """

""" #3
lst=["Aman","Rahul","Anjali","Priya","Akash"]
a=(list(filter(lambda z: z.startswith("A") ,lst)))
print(a) """


""" #4
lst=["cat","elephent","dog","tiger","hippotamus"]
long=list(filter(lambda l: len(l)>5 ,lst))
print(long) """


""" #5
salary={"sagar":50000, "bharat":60000, "guddu":4000, "shruti":30000,"shreya":100000}
s=list(filter(lambda x: x[1]>40000 , salary.items()))
print(s) """

