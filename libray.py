print("*** Libray Management System ***")
print("1.book issue System")
print("2.Libray Fine System")
print("3.membership Verification")
print("4.Maximum book limit check")
print("5.exit")
choice=int(input("enter your choice:-"))
match choice:

    case 1:
        book_name=input("enter book name:-")
        copies=int(input("enter number of copies:-"))
        if copies>0:
            print("available copies=",copies)
            print("you can issue book")
        else:
            print("you cannot issue book")


    case 2:
        last_day=int(input("enter last days:-"))
        if last_day<3:
            print("no fine")
        else:
            fine=last_day*10
            print("fine amount=",fine)

    case 3:
        status=input("enter membership (active/inactive) :-")
        if status.lower()=="active":
            print("book borrowing allowed ")
        else:
            print("book borrowing not allowed")


    case 4:
        book=int(input("enter number of borrowed book:-"))
        if book >3:
            print("you can't borrow more books")
        else:
            print("you can borrow book")
            print("borrow book succesfully")

    case 5:
        exit(0)


    case _:
        print("invalid input")           







