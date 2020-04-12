class Page:
    def __init__(self, num, content):
        self.num = num
        self.content = content
    def output(self):
        return f'{self.content}'

title_page = Page(0, 'Python fPractice Book')
print(type(title_page))

print(isinstance(title_page,Page))

print(dir(title_page))