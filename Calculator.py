number1=float(input("Enter first number: "))
number2=float(input("Enter second number: "))
print("\n")
print("1. Enter + for addition\n")
print("2. Enter - for substraction\n")
print("3. Click * for multliplication\n")
print("4. Click / for division\n")

choice=input("Enter your choice for operation: ")

print("\n")

if choice=="+":
    result=number1+number2
    print("The addition of number1 and number2 is: ", result)

elif choice=="-":
    result=number1-number2
    print("The substraction of number1 and number2 is: ", result)

elif choice=="*":
    result=number1*number2
    print("The multliplication between number1 and number2 is: ", result)

elif choice=="/":
    if number2==0:
        print("Invalid Result")
    else:
        result=number1/number2
    print("The division of number1 and number2 is: ", result)

else:
    print("Invaldi choice please enter the valid operation")




