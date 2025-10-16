# employee={"id":1,
#            "name": "ali", 
#            "salary": 5000.50
#            }

# print("employess details as follows:")
# for key,value in employee.items():
#     print(key,"->" ,value)
# #adding key in dictionary
# employee["city"]="muscat"
# print('\ndictionary after adding city')

# for key,value in employee.items():
#     print(key,"->",value)

# del employee["salary"]
# print("\n employee details after deleting salary \n")
# for key,value in employee.items():
#     print(key,"->",value)

employee={"id":1,
           "name": "ali", 
           "salary": 5000.50
           }
print('all keys from employee ')
for k in employee.keys():
    print(k,end="\t")

print('all values from employee ')
for v in employee.values():
    print(v,end="\t")

print('\n key:values \n')
for k,v in employee.items():
    print(k, ":", v)

print('\n dictionary as follows')
print(employee)

del employee ["salary"]
print('after deleting salary')
for k,v in employee.items():
    print(k,":",v)