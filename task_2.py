class MyMeta(type):
    a = {}

    def __call__(cls):
        if cls not in cls.a:
            cls.a[cls] = super(MyMeta, cls).__call__()
        return cls.a[cls]


class Test(metaclass=MyMeta):
    pass


x = Test()
y = Test()
print(x is y)
