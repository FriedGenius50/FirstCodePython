print("1. Addition");
print("2. Subtraction");
print("3. Multiplication");
print("4. Division");
print("5. Factorial");
print("6. Exit");
choice = int(input("Enter your choice: "));
if (choice>=1 and choice<=4):
    print("Enter two numbers: ");
    num1 = int(input());
    num2 = int(input());
    if choice == 1:
    	res = num1 + num2;
    	print("Result = ", res);
    elif choice == 2:
    	res = num1 - num2;
    	print("Result = ", res);
    elif choice == 3:
    	res = num1 * num2;
    	print("Result = ", res);
    else:
    	res = num1 / num2;
    	print("Result = ", res);
elif choice == 6:
    exit();
elif choice == 5:
        print ("Please enter an integer above zero")
        X = int(input("Enter an integer for x: "))
        R = int
        C = int
        P = int
        Y = int
        Y = X
        P = 1
        if X > 0:
            for i in range (X):
                R = Y
                C = R-1
                P = R*P
                Y = Y-1
                #print(X,Y,R,C)
            print (X,"! =",P)
            print (P)


        else:
            print ("ERrOR")
