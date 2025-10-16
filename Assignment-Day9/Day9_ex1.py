#write program using function to find greatest of three number entered by user
#write the solution in assignment folder with name day-9_ex1.py
#push on github
#share github link in chat once done

# define function
def find_greatest(num1,num2,num3):
     if num1 >= num2 and num3 >= num3:
         return num1
     elif num2 >= num1 and num2 >= num3:
         return num2
     else:
         return num2

# input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

greatest = find_greatest(num1, num2, num3)
print(f"The greatest number is: {greatest}")

print('---------------------------------------')

