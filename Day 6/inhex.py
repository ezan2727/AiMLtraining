# # super class or base class or parent class
# class emp:
#     def reg(self,id,name):
#         self.id=id
#         self.name=name

#  def display(self):
#    print('ID:',self.id)
#    print('Name:',self.name)
# #inheritence class or derived class or child class
# class Dev(emp):
#     def welcome(self):
#         print('Welcome to developer')
           
# dev1=Dev()
# dev1.reg(101,'Andi')
# dev1.display()
# dev1.welcome()

# emp1=emp()
# emp1.reg(102,'Budi')
# emp1.display()

#Super class or base class or parent class
# class Emp:
#     def reg(self, id, name):
#         self.id=id
#         self.name=name

#     def display(self):
#         print('Id: ',self.id)
#         print('Name: ',self.name)

# #Inheritence class or derived class or child class
# class Dev(Emp):
#     def welcome():
#         print('Welcome to developer')

# d=Dev()
# d.welcome=()
# d.reg(1,'Sam')
# d.display()

# e=Emp()
# e.reg(102,'Sara')
# e.display()

class emp:
    def reg(self):
        self.id=int(input('Enter ID:'))
        self.name=input('Enter Name:')

    def display(self):
        print('name:',self.name)
        print('id:',self.id)

class dev(emp):
    def reg(self):
        super().reg()
        self.domain=input('Enter Domain:')

    def display(self):
        super().display()
        print('Domain:',self.domain)

d1=dev()
d1.reg()
d1.display()
