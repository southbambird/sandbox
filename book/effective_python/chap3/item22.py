def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{message}: {values_str}')
log('My number are ', [1, 2])
log('Hi there', [])  #空配列渡さないといけない、いまいち


def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{message}: {values_str}')
log('My number are ', 1, 2)
log('Hi there')  #余分な値渡さなくて良い

#問題1:メモリ大量消費
def my_generator():
    for i in range(10):
        yield i
def my_func(*args):
    print(args)
it = my_generator()
my_func(it)  #ここでジェネレータをタプルに展開するので、メモリ食いつぶす可能性あり

#問題2:引数追加する場合、呼び出し元も修正する必要あり
def log(sequence, message, *values):
    if not values:
        print(f'{sequence} - {message}')
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{sequence} - {message}: {values_str}')
log(1, 'Favorites', 7, 33)
log(1, 'Hi there')
log('Favorite numbers', 7, 33) #->古い呼び出し方は意図しない動きをする（エラー発生しないので気づきづらい）
