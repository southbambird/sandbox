def test_deco(func):
    def new_func(*args, **kwargs):
        print("decorator message!")
        result = func(*args, **kwargs)
        print("decorator done.")
        return result
    return new_func

def add_ints(a, b):
    print("add!!")
    return a + b

#print(add_ints(3,4))

deco_add_ints = test_deco(add_ints)
print(deco_add_ints(3,4))