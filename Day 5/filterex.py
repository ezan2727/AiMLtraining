numbers=[10,25,30,40,2,1]

print('original list')
for n in numbers:
    print(numbers,end=" ")

even_numbers=list(filter(lambda x:x%2==0,numbers))

print('\neven numbers')
for num in even_numbers:
    print(num,end=" ")

#You have following list
#write code using filter to find out all the number less than 5 from the list

# our_list=[4,2,5,6,7,3,1,10]
# print('Original List\n')
# for num in our_list:
#     print(num,end=" ")

# our_numbers= list(filter(lambda x: x<5, our_list))

# print('\nNumbers less than 5 from list as follows\n')
# for num in our_numbers:
#     print(num,end=" ")

#     students_marks={ 'sam': 90, 
#                     'james': 67, 
#                     'linda': 45, 
#                     'mike': 78, 
#                     'anna': 88}
    
# print('all students')
# for k,v in students_marks.items():
#      print(f'name: {k} marks: {v}')

# pass_students=dict(filter(lambda x:x[1]>=50, students_marks.items()))
        
# print('passed_students')
# for k,v in pass_students.items():
#     print(f'name: {k} marks: {v}')
            
# sort_pass_students=dict(sorted(pass_students.items(),key=lambda x:x[1]))
# print('ascending order')
# for k,v in sort_pass_students.items():
#     print(f'name: {k} marks: {v}')

# sort_pass_students_desc=dict(sorted(pass_students.items(),key=lambda x:x[1],reverse=True))

# print('descending order')
# for k,v in sort_pass_students_desc.items():
#     print(f'name: {k} marks: {v}')