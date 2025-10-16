def add(num1,num2):
    return num1+num2

def multi(num1,num2):
    return num1*num2

def avg(num1,num2):
    return num1+num2/2

def multisub(num1,num2):
    return num1-num2

def div(num1,num2):
    return num1/num2
print("wecome to our calculator")
while True:
    print('select operation \n1.add \n2.subb. \n3.multi. \n4.division \n5.average \n6.exit')
    op=int(input('enter your operation choice:(1-6):\t'))
    if(op==6):
        print('bye')
        break
    if((op>=6)) or (op<=0):
        print('wrong opration choice only 1 to 6 are allowed')
        break
    else:
        fnum=float(input('enter first number:\t'))
        snum=float(input('enter second number:\t'))
    if(op==1):
        print(f'result after adding{fnum},{snum}:\t',add(fnum,snum))
    elif(op==2):
        print(f'result after subtracting {snum} from {fnum} :\t',sub(fnum,snum))
    elif(op==3):
        print(f'result after multiplying{fnum},{snum} :\t',multi(fnum,snum))
    elif(op==4):
        print(f'result after dividing{fnum}by{snum}:\t',div(fnum,snum))
    elif(op==5):
        print(f'average of {fnum} and {snum}:\t',avg(fnum,snum))
    else:
        print('wrong operation choice,please choose only 1 to 6')

        

