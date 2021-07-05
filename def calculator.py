def calculator():
    print("calculator")


    operators = input('''
    + for additon
    - for subtraction
    * for multiplication
    / for divison
    ** for power
    % for reminder
    ''')
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))

    if operators == "+":
        if num1 == 56:
            print('77')
        else:
            print(f"{num1}+{num2}={num1+num2}")
    elif operators == "-":
        print(f"{num1}-{num2}={num1-num2}")
    elif operators == "*":
        if num1 == 45:
            print('555')
        else:
            print(f"{num1}*{num2}={num1*num2}")
    elif operators == "/":
        if num1 == 56:
            print('4')
        else:
            print(f"{num1}/{num2}={num1/num2}")
    elif operators == "**":
        print(f"{num1}power{num2}={num1**num2}")
    elif operators =="%":
        print(f"{num1}%{num2}={num1%num2}")
    else:
        print("you enter the invalid")
    again()

def again():
    cal_again=input('''
    do you want to do it again
    ''')
    if cal_again=='Y':
        calculator()
    elif cal_again=='N':
        print("thanks for using this")
    else:
        print("enter only Y or N")

calculator()




