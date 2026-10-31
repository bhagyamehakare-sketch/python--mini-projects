while True:
    try:
        a=int(input("enter first number:"))
        b=int(input("enter second number:"))

        print("what kind of operatio you want to perform press + for addition \n press - for subtraction\n press / for division \n press * for multiplication")
        o=input("enter operation:")

        match o:
            case"+":
                print(f"The result is ,{a+b}")
            case "-":
                print(f"The result is,{a-b}")
            case "*":
                print(f"the result is,{a*b}")
            case _ :
                print("invalid casse")
    except Exception as e:
        print(f"enter valid number,{e}")