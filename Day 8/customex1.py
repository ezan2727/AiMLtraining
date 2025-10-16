class invalidage(Exception):
    pass
def checkage(age):
    if age<0:
        raise invalidage('age should be greater than 18')
    elif age<18:
        raise invalidage('age should be not less than 50')
    elif age>=50:
        raise invalidage('sorry, you are not required for this job')
    else:
        print(f'age{age} is accepted and valid for this job')

try:
    age=int(input("Enter your age: "))
    checkage(age)
except invalidage as e:
    print('invalid age:', e)
except Exception as ex:
    print('error!')
#     print("Thank you")
