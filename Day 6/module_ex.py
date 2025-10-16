# import math
# print(math.sqrt(16))
# print(math.factorial(5))
# print(math.pi)
# print(math.pow(2, 3))

# import inspect
# import datetime

# print('today is (date):', datetime.date.today())

# datetimeclass=inspect.getmembers(datetime,inspect.isbuiltin)
# print('all class inside datetime module')

# for n,function in datetimeclass:
#     print(n)
# print('---------------------')

# functions=inspect.getmembers(datetime.inspect.isbuiltin)
# for n,function in functions:
#     print(n)
# print('---------------------')

# number=[1,2,3,4,5,6,7,8,9]
# print('max number is:',max(number))
# print('min number is:',min(number))
# for n in number:
#     print(n)

import os
dirs=os.listdir('.')
for dr in dirs:
    print(dr)
print('---------------------')

print('current working directory is:',os.getcwd())
print('---------------------')

os.mkdir('newdir')
os.rmdir('newdir')
print('newdir created and removed')
print('---------------------')
