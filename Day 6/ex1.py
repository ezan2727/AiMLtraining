# class player:
#     def __init__(self):
#         print("welcome to player class")

#     def reg(self,id,name,team):
#         self.id=id
#         self.name=name
#         self.team=team
        
#     def display(self):
#         print("player id:",self.id)
#         print("player name:",self.name)
#         print("player team:",self.team)

# #object creation
# p1=player()
# p2=player()
# p3=player()
# p1.reg(1,'sachin','india')
# p2.reg(2,'ponting','australia')
# p3.reg(3,'kallis','south africa')
# p1.display()
# p2.display()
# p3.display()

class player:
    def __init__(self,id,name,team):
        self.id=id
        self.name=name
        self.team=team
        
    def display(self):
        print(f'id: {self.id}, name: {self.name}, team: {self.team}')
    def __str__(self):
        return f'id: {self.id}, name: {self.name}, team: {self.team}'

#object creation
p1=player(1,'sachin','india')
p2=player(2,'ponting','australia')
p3=player(3,'kallis','south africa')
#displaying first player details
# p1.display()
# p2.display()
# p3.display()

print(p1)
print(p2)
print(p3)