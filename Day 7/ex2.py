# import random

# print('Random number between 1 and 1000:')
# print(random.randint(1, 1000))

# import random
# print('welcome to the lottery')

# lottery_numbers = random.sample(range(1, 100), 6)
# print('Your lottery numbers are:', lottery_numbers)
# if set(lottery_numbers) == {3, 11, 24, 36, 37, 42}:
#     print('Congratulations! You have won the lottery!')

# elif set(lottery_numbers).intersection({3, 11, 24, 36, 37, 42}):
#     print('You have some matching numbers. Better luck next time!')
# else:
#     print('No matching numbers. Try again!')

import random
def winner():
    name = input("Enter your name: ")
    lucky_number = random.randint(1)
    
    print(f'Hello, {name}! Your lucky number is {lucky_number}.')
    return lucky_number
if winner() == 50:
    print("Congratulations! You are the winner!")
else:
    print("Sorry, better luck next time!")
# import random
