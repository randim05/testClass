class SchoolMember:
    pop = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.tell()

    def tell(self):
        print('Я {0}, мне {1} лет'.format(self.name, self.age))


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print("Создан новый учитель {}".format(self.name))

    def tell(self):
        SchoolMember.tell(self)


class Stydent(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print("Создан новый ученик {}".format(self.name))

    def tell(self):
        SchoolMember.tell(self)


teach1 = Teacher("Мариванна", 40, 20000)
stud1 = Stydent("Раздолбай", 15, 75)

teach1.tell()
stud1.tell()