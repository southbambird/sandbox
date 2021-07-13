def knights2(saying):
    def inner2():
        return f"We are the knights who say: '{saying}'"
    return inner2

def hoge(count):
    def inner():
        print(count)
        ++count
    return inner

test = hoge(3)
test()
test()