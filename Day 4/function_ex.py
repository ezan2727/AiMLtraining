# def function_name(parameters):
#     '''docstring'''
#     statement(s)

# #function without parameters
# def welcome():
#     print("welcome to function")
#     print("our first function")

# welcome()

# #function with a parameters
# def welcome(name):
#     print("welcome to function in python mr.\\ms", name)

# username=input('enter your name: \t')
# #function
# welcome(username)

#function with parameter and return

def add(num1,num2):
    return num1+num2

fnum=int(input("enter first number"))
snum=int(input("enter second number"))
print(f'result after adding {fnum} and {snum} is =\t', add(fnum,snum))

