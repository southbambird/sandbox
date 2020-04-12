def get_book(index):
    items = ['note','notebook','sketchbook']
    try:
        book = items[index]
    except (IndexError,TypeError) as e:
        print(f'例外が発生しました: {e}')
    else:
        print('問題なく処理が完了しました')
        return book

get_book(1)
