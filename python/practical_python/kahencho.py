def print_pages(content, *args):
    print(content)
    for more in args:
        print('more:', more)

print_pages('my content')

print_pages('my content','hoge1', 'hoge2')


def print_pages2(content, **kwargs):
    print(content)
    for key, value in kwargs.items():
        print(f'{key}: {value}')

print_pages2('my content2')

print_pages2('my content2', hoge1='hoge1', hoge2='hoge2')