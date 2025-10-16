from ourpack import calc
try:
    fnum=float(input("Enter first number: "))
    snum=float(input("Enter second number: "))
    op=input("Enter operation (+, -, *, /): ")

    if op == '+':
        result = calc.add(fnum, snum)
    elif op == '-':
        result = calc.subtract(fnum, snum)
    elif op == '*':
        result = calc.multiply(fnum, snum)
    elif op == '/':
        result = calc.divide(fnum, snum)
    else:
        raise ValueError("Invalid operation")
    print(f'Result after {op} {fnum} and {snum} is: {result}')
    
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError as ve:
    print("Error:", ve)
except Exception as e:
    print("An unexpected error occurred:", e)

choice=input("Do you want continue? if yes press y/Y else n/N: ")
if choice=='y' or choice=='n':
    if choice=='y':
        print("continue")
    else:
        print("bye")