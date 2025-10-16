#take user marks from user with in 0 to 50
#if user enter outside [0-50] raise error invalidmarks using custom exception
#give change to user till, he/she entered valid marks

# class InvalidMarks(Exception):
#     pass

# while True:
#     try:
#         marks = int(input("Enter your marks (0-50): "))
        
#         if marks < 0 or marks > 50:
#             raise InvalidMarks("Marks must be between 0 and 50!")
#         print(f"Valid marks entered: {marks}")
#         break

#     except InvalidMarks as e:
#         print(e)
#     except ValueError:
#         print("Please enter a valid number only!")

class InvalidMarks(Exception):
    pass

def check_marks(marks):
    if marks<0:
        raise InvalidMarks('marks should not be negative')
    elif marks>50:
        raise InvalidMarks('marks should be within range 0-50')
    else:
        print(f'user {marks}, your marks is qualified')

while True:
    try:
        usermarks=int(input('please enter your name:'))
        marks=int(input("Enter your marks (0-50): "))
        marks.check_marks(usermarksmarks)
    except mark.InvalidMarks as e:
        print('InvalidMarks:',e)
    except Exception as e:
        print('error',ex)
    else:
        print('recorded')
        break
    choice=input("do you wanna re-enter marks?, id yes press y/Y, else n/N :")
if choice=='y' or choice=='n':
    if choice=='y':
        print("continue")
    else:
        print("bye")
