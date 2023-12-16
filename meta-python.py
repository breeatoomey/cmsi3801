class MyMeta(type):
    def __new__(cls, name, parents, dct):
        print("A new class named %s" % name)
        return super(MyMeta, cls).__new__(cls, name, parents, dct)
class MyClass(metaclass=MyMeta):
    pass
m1 = MyClass()
print(type(m1))