print(" -----Calculater---- ")
a=int(input("Enter the first number :"))
op=input("Enter the opertion to perfrom  ('+','-','*','/')")
b=int(input('"Enter the second number :'))

if op=='+':
    result= a+b
    print("addition :-",result)
elif op=='-':
    result= a-b
    print("Subtration :-",result)
elif op=='*':
    result= a*b
    print("mulitipilcation :-",result)
elif op=='/':
    if b!=0:
       result= a/b
       print("Divisoon :-",result) 
    else:
        print("Zero is not divisibly")
else:
    print("Invaild choice")

 