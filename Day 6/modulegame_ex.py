import inspect
import game

class player:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print('name:',self.name)
        print('age:',self.age)
p1=player('Alice',30)
p1.display()
print('---------------------')
