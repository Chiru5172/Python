f=float(input("Enter first number: "))
s=float(input("Enter second number: "))
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modular Division")
print("6.Floor Division")
print("7.Exponentiation")
n=int(input("How many operations: "))
for c in range(n):    
    c=int(input("Enter your choice: "))
    if c==1:
        print("Sum of ",f," and ",s," : ",f+s)
    elif c==2:
        print("Difference of ",f," and ",s," : ",f-s)
    elif c==3:
        print("Product of ",f," and ",s," : ",f*s)
    elif c==4:
        if s!=0:
            print("Division of ",f," and ",s," : ",f/s)
        else:
            print("Invalid")
    elif c==5:
        if s!=0:
            print("Remainder of ",f," and ",s," : ",f%s)
        else:
            print("Invalid")
    elif c==6:
        if s!=0:
            print("Floor Division of ",f," and ",s," : ",f//s)
        else:
            print("Invalid")
    elif c==7:
        print("Exponentiation of ",f," and ",s," : ",f**s)
    else:       
        print("Enter a number from 1 to 7")
