class Robots():
    population = 0
    def __init__(self, name):
        self.name = name
        print("Созданн {}".format(self.name))
        Robots.population += 1

    def sayHi(self):
        print("{} говорит привет!".format(self.name))

    def dyi(self):
        print("{} уничтожен".format(self.name))
        Robots.population -= 1

        if Robots.population == 0:
            print("Это был последний")
        else:
            print("Осталось {}".format(Robots.population))

    @classmethod
    def howmach(cls):
        print("Сейчас есть {:d} роботов".format(cls.population))


r2 = Robots("R2-D2")
r2.sayHi()
c3 = Robots("C3PO")
c3.sayHi()
c3.dyi()
r2.howmach()
r2.dyi()
r2.howmach()