class student:
    def __init__(self, id,name):
        self.name = name
        self.id = id

    def print_details(self):
        print(f'student name is {self.name} and id is {self.id}')

        