class Person:
    def __init__(self, name='default'):
        self.name = name

    def sayHi(self):
        print("hello", self.name)


a = Person("Dimas")
b = Person()
a.sayHi()
b.sayHi()
