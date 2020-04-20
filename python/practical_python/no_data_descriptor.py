class TextField:
    def __init__(self, value):
        if not isinstance(value, str):
            raise AttributeError('must be str')
        self.value = value
    def __set_name__(self, owner, name):
        print(f'__set_name__ was called')
        print(f'{owner}, {name}')
        self.name = name
    def __get__(self, instance, owner):
        print('__get__ was called')
        return self.value

class Book:
    title = TextField('Python Practice Book')

book = Book()
print(book.title)
book.title = 'Book'
print(book.title)