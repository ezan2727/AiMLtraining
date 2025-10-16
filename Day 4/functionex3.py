#defult parameter in function
# def info(id,name,city='KL')
#     print(f"details as follows \n ID :{id} name: {name} city: {city}")

#     info(1,'sam','new delhi')
#     indo(101,'xi')
#     info(103,'chang')
#     we want to create a single method that can able to add 2 numbers,3,numbers,4 numbers, or numbers 
# and return correct total

# def add(n1,n2=0,n3=0,n4=0, n5=0)
#     return n1+n2+n3+n4+n5

# print("result: ",add(1,2))
# print("result: ",add(5,3,1,4,10))
# print("result: ",add(5,25,10))

# def add(*nums):
#     return sum(nums)

# print('sum of 1,10,11 is :\t', add(1,10,11))
# print('sum of 5,3 is :\t', add(5,2))
# print('sum of 10,10,100,100,200,219,19 is :\t', add(10,10,100,100,200,219,19))

def add(*nums):
    return sum(nums)

print ('maximum example')
print('maximum of 1,10,11 is :\t', max(1,10,11))
print('maximum of 5,3 is :\t', max(5,2))
print('maximum of 10,10,100,100,200,219,19 is :\t', max(10,10,100,100,200,219,19))

print ('minimum example')
print('min of 1,10,11 is :\t', max(1,10,11))
print('min of 5,3 is :\t', max(5,2))
print('min of 10,10,100,100,200,219,19 is :\t', max(10,10,100,100,200,219,19))



