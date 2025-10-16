# class employee:
#     def display(self):
#         print("This is employee class")

# object=employee()
# object.display()

# #class classname:
# #    def of class
# #    attributes methods,constructor

# #objectname=classname()
# #objectname.methodname()

# e=employee()
# e.display()

#second example
class employee:
    def register(self,id,name):
        self.id=id
        self.name=name

    def display(self):
        print("Employee details as follows:")
        print("ID:",self.id)
        print("Name:",self.name)

e1=employee()
e1.register(101,'Amirah')
e1.display()
e2=employee()
e2.register(102,'Aisyah')
e2.display()