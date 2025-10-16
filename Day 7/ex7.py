try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
    print(f"sum of {num1} and {num2} = {result}")
except Exception as e:
    print('error:', e)
finally:
    print('end of program')
    