import math
import inspect
#num=int (input("Enter a number to find its square root: "))
def square_root(num):
    """Returns the square root of a number."""
    return math.sqrt(num)
print(square_root(16))
print(inspect.getdoc(square_root))
print(inspect.getsource(square_root))

#print(f"The square root of {num} \t, round(math sqrt(num),2)

