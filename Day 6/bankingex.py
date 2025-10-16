# class account:
#     def __init__(self,accno,name,balance):
#         self.accno=accno
#         self.name=name
#         self.balance=balance

#     def deposit(self,amount):
#         self.balance+=amount
#         print('balance after deposit:',self.balance)
#     def withdraw(self,amount):
#         if(self.balance>=amount):
#             self.balance-=amount
#             print('balance after withdraw:',self.balance)
#         else:
#             print('insufficient balance')
#             print('transaction failed!')
#     def display(self):
#         print(f'Account number: {self.accno}, Name: {self.name}, Balance: {self.balance}')

# class account:
#     def __init__(self,ac_holder, balance):
#         self.ac_holder=ac_holder
#         self.balance=balance

#     def deposit(self,amount):
#         self.balance+=amount
#         print('balance after deposit:',self.balance)

#     def withdraw(self,amount):
#         if(self.balance>=amount):
#             self.balance-=amount
#             print('balance after withdraw:',self.balance)
#         else:
#             print('insufficient balance')
#             print('transaction failed!')
#     def show(self):
#         print(f'Account number: {self.ac_holder}, Balance: {self.balance}')

# #object creation
# ac1=account('Andi',1000)
# ac1.show()
# ac1.deposit(500)
# ac1.withdraw(200)

# print('-------------------')

# ac2=account('Budi',2000)
# ac2.show()
# ac2.deposit(1000)
# ac2.withdraw(5000)

# if(__name__=="d"):
#     deposit_amount=float(input('Enter amount to deposit:'))
#     ac1.deposit(deposit_amount)
# elif(__name__=="w"):
#     withdraw_amount=float(input('Enter amount to withdraw:'))
#     ac1.withdraw(withdraw_amount)
# elif(__name__=="s"):
#     ac1.show()
# else:
#     print('Invalid option')


