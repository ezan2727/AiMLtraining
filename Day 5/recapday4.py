# def display():
#     print('Welcome to recap of functions')

# display()

# #Example 2 functions (letak nama)
# def welcome(name):
#     print('Welcome to functions Mr.\\Ms.', name)

# welcome('Amirah')

# #Example 3 (letak nombor Cube)
# def cube(num):
#     cube_num=num*num*num
#     print(f'Cube of given number: {num} is =\t {cube_num}')

# my_num=int(input('Enter number to find out Cube:\t'))
# cube(my_num)

# #Example 4 (semua  di atas)
# def welcome(name):
#     print('Welcome to functions Mr.\\Ms.', name)

# def cube(num):
#     cube_num=num*num*num
#     print(f'Cube of given number: {num} is =\t {cube_num}')

# def square(num):
#     return num*num

# username=input('Enter User Name: \t')
# my_num=int(input('Enter number to find out cube and square: \t'))

# welcome(username)
# cube(my_num)
# sq=square(my_num)
# print(f'Square of {my_num} is {sq}')

# my_sal=float(input('enter salary to find out bonus: \t'))
# bonus=salbonus(my_sal)
# print(f'salary {my_sal} bonus: {bonus}')
# print(f'salary after bonus = \t',(my_sal+bonus))

def salbonus(salary):
    bonus = salary * 0.10
    return bonus

my_sal = float(input('enter salary to find out bonus: \t'))
bonus = salbonus(my_sal)
print(f'salary {my_sal} bonus: {bonus}')
print(f'salary after bonus = \t', (my_sal + bonus))