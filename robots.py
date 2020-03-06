class Robots:
    population = 0

    def __init__(self, name):
        self.name = name
        print("Созданн {}".format(self.name))
        Robots.population += 1

    def say_hi(self):
        print("{} говорит привет!".format(self.name))

    def dyi(self):
        print("{} уничтожен".format(self.name))
        Robots.population -= 1
        if Robots.population == 0:
            print("Это был последний")
        else:
            print("Осталось {}".format(Robots.population))

    @classmethod
    def how_many(cls):
        print("Сейчас есть {:d} роботов".format(cls.population))


r2 = Robots("R2-D2")
r2.say_hi()
c3 = Robots("C3PO")
c3.say_hi()
c3.dyi()
r2.how_many()
r2.dyi()
Robots.how_many()
