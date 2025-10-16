class bird:
    def fly(self):
        print("Bird can fly")

class airplane:
    def fly(self):
        print("Airplane can fly")

b=bird()
print('Bird implement')
b.fly()

a=airplane()
print('Airplane implement')       
a.fly()

print('using for loop')
for obj in (b,a):
    obj.fly()



