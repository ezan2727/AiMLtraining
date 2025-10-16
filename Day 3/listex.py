# print("List Example One")

# my_list = [10, 20, 30, "Python",None,True,12.45,'Ravi']
# print('Number of items in list are:',len(my_list))

# for item in my_list:
#     print(item)

# print("Second Example of List")
# emps=["Sam","Ravi","Ani","Zoya","Vi","Sa","Chang","Neha"]
# print("Number of Employees",len(emps))
# print('All Employees')
# # for emp in emps:
# #     print(emp)

# # print(emps)

# for emp in emps:
#     print(emp,end=" ")


# #Sort Example
# #listName.sort()
# emps.sort()
# print("\n List after sorting")
# for e in emps:
#     print(e, end=" ")
   
# #Reverse example
# #listName.reverse()
# emps.reverse()
# print('\n Employees in Descending Order')
# for e in emps:
#     print(e, end=" ")

# # append,remove,pop insert method

# emps=["sam","ravi","ani","zoya","vi","sa","chang","neha"]
# print("Number of Employees",len(emps))
# for emp in emps:
#     print(emp,end=" ")

    #append : adds the item at the end of list
# newEmp=input("\nEnter employee name to add in list:\t")
# emps.append(newEmp)
# print('\nAfter adding New Employee: Number of employees are:',len(emps))
# for emp in emps:
#     print(emp,end=" ")

#insert(index,item): This will add item at  given index
# newEmp=input("\nEnter employee name to add in list:\t")
# pos=int(input("Enter poistion where you want to insert inside list:\t"))
# emps.insert(pos,newEmp)
# print('\nAfter adding New Employee: Number of employees are:',len(emps))
# for emp in emps:
#     print(emp,end=" ")

# append,remove,pop insert method

# emps=["sam","ravi","ani","zoya","vi","sa","chang","neha"]
# print("Number of Employees",len(emps))
# for emp in emps:
#     print(emp,end=" ")
# #listName.remove(item): Will remove item from the list.
# delEmp=input('Employee to remove from the list:\t')
# if delEmp in emps:
#     emps.remove(delEmp)
#     print(f"Number of Employees after deleting {delEmp} in list are:",len(emps))
#     for emp in emps:
#         print(emp,end=" ")
# else:
#     print(f'No such item {delEmp} in employee list')

#pop() example
#listName.pop(index): Will delete element at given index  and return its value.
# emps=["sam","ravi","ani","zoya","vi","sa","chang","neha"]
# print("Number of Employees",len(emps))
# for emp in emps:
#     print(emp,end=" ")

# del_index=int(input('Enter Index to pop item:\t'))
# print('Pop Result: ',emps.pop(del_index))
 
# print("Number of Employees after pop() are:",len(emps))
# for emp in emps:
#     print(emp,end=" ")

#find out first and last element from the list
emps=["sam","ravi","ani","zoya","vi","sa","chang","neha"]
print("Number of Employees",len(emps))
for emp in emps:
    print(emp,end=" ")
count=len(emps)
print('\n First Element of employees list is: ',emps[0])
print('\n Last Element of employees list is: ',emps[-1])
print('\n second Last Element of employees list is: ',emps[-2])
print('\n Last Element of employees list is: ',emps[count-1])
