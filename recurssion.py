def add(a):
    if a>0:
        print(a)
        a=a-1
        add(a)
    else:
        print("It is over")
a= int(input("Enter first number: "))
add(a)
