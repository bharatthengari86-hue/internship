purchase_amount=int(input("enter purchase amount:-"))
if(purchase_amount>10000):
    discount=purchase_amount/20
    print("original amount=",purchase_amount)
    print("discount amount=",discount)
elif(purchase_amount>5000):
    discount=purchase_amount/10
    print("original amount=",purchase_amount)
    print("discount amount=",discount)
elif(purchase_amount>2000):
    discount=purchase_amount/0.5
    print("original amount=",purchase_amount)
    print("discount amount=",discount)
else:
    print("no discount")