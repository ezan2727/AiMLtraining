class emp:
    def __init__(self,id,name,qualification):
        self.id=id
        self.name=name
        self.qualification=qualification

    def display(self):
        print('id:', self.id)
        print('name:', self.name)
        print('qualification:', self.qualification)

class dev(emp):
    def __init__(self,id,name,qualification,domain,project):
        super().__init__(id,name,qualification)
        self.domain=domain
        self.project=project

    def display(self):
        super().display()
        print('domain:',self.domain)
        print('project:',self.project)

       
#create one emp object with id=1, name='John', qualification='B.Tech'

#create one dev object with id=2, name='Alice', qualification='M.Tech', domain='AI', project='Chatbot'

#display emp details

#display dev details

# e=emp(1,'John','B.Tech')
# e.display()
# print('-------------------')
# d=dev(2,'Alice','M.Tech','AI','Chatbot')
# d.display()
# print('-------------------')

e=emp(1,'John','B.Tech')
e.display()

d=dev(2,'Alice','M.Tech','AI','Chatbot')
d.display()
