# db = {
#     'bob': {'pay': 30000, 'job': 'dev', 'age': 42, 'name': 'Bob Smith'},
#     'sue': {'pay': 44000.0, 'job': 'hdw', 'age': 45, 'name': 'Sue Jones'},
#     'tom': {'pay': 0, 'job': None, 'age': 50, 'name': 'Tom Tom'}
# }


class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job


if __name__ == '__main__':
    bob = Person('Bob Smith', 42, 30000, 'software')
    sue = Person('Sue Jones', 45, 40000, 'hardware')
    print(bob.name, sue.pay)
    print(bob.name.split()[-1])
    sue.pay *= 1.10
    print(sue.pay)
