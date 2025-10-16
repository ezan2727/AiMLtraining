# def factorial(num):
#     if((num==0)or(num==1)):
#         return 1
#     else:
#         return num*factorial(num-1)
    

# num=int(input('enter a number to find out factorial:'))
# print(f'factorial of {num} is=', factorial(num))

#write a python function which converts inches to cms.
# 1 inch =2.5 cm

# def inch_to_cm(num):
#     return num*2.5

# num=int(input('enter inchies:'))
# print(f'{num} inchies are equal to {inch_to_cm(num)} cm')

def inch_to_cm(inch):
    return inch*2.5

num=int(input('enter inchies:'))
print(f'{num} inchies are equal to {inch_to_cm(num)} cm')

#write a function to find out the table of given number
def gen_table(num):
    for i in range(1,11)
    print(f'{num}*{i}=\t {(num*i)}')

number=int(input('enter number to find out table'))
gen_table(number)