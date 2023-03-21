class Book:
    def __init__(self, name_input, author_input):
        self.name = name_input
        self.author = author_input

    def __repr__(self):
        return f'{self.author}: {self.name}'