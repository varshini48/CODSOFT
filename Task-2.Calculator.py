print("choose what you want to perform")
while True:
    
    print("1. ADD")
    print("2. SUBTRACT")
    print("3. MULTIPLY")
    print("4. DIVISION")
    print("5. QUIT")
    choice=int(input("enter your choice: "))
    result=0
    if choice in [1,2,3,4]:
        
        if choice==1:
            num1=float(input("enter number: "))
            num2=float(input("enter number: "))
            result=num1+num2
        elif choice==2:
            num1=int(input("enter number: "))
            num2=int(input("enter number: "))
            result=num1-num2
        elif choice==3:
            num1=int(input("enter number: "))
            num2=int(input("enter number: "))
            result=num1*num2
        elif choice==4:
            num1=int(input("enter number: "))
            num2=int(input("enter number: "))
            if num2 == 0:
                print("Cannot divide by zero.")
                continue
            result=num1/num2
        print(f"The result is {result} ")
    elif choice==5:
            print("see you again")
            break
        
    else:
        print("invalid")
    

    
        
        
    
