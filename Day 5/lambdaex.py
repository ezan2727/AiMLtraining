# def add(a,b)
#     total=a+b
#     return total

# result=add(12,15)
# print(result)

# addition=lambda a,b:a+b
# multiply=lambda a,b:a*b
# div=lambda a,b:a/b
# avg=lambda a,b:(a+b)/2
# sub=lambda a,b:a-b

# num1=int(input('Enter first number:\t'))
# num2=int(input('Enter second number:\t'))

# print('multiplication result:',multiply(num1,num2))
# print('subtraction result:',sub(num1,num2))

# print('division result:',div(num1,num2))

check_odda=lambda n : "odd number" if n%2==1 else "even number"
num=int(input('Enter number to check even or odd:\t'))
print(check_odda(num))

