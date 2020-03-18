# db = {
#     'bob': {'pay': 30000, 'job': 'dev', 'age': 42, 'name': 'Bob Smith'},
#     'sue': {'pay': 44000.0, 'job': 'hdw', 'age': 45, 'name': 'Sue Jones'},
#     'tom': {'pay': 0, 'job': None, 'age': 50, 'name': 'Tom Tom'}
# }
from tkinter import *
# import tkinter
import shelve


def reply():
    Message.info(title='popup', message='Button pressed!')  #not work


window = Tk()
button = Button(window, text='press', command=reply)
button.pack()
window.mainloop()


class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay *= (1.0 + percent)

    def __str__(self):
        return (' < % s = > % s: % s, % s > ' %
                (self.__class__.__name__, self.name, self.job, self.pay))


class Manager(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, "Manager")

    def give_raise(self, percent, bonus=0.1):
        Person.give_raise(self, percent + bonus)


bob = Person('Bob Smith', 44)
sue = Person('Sue Jones', 47, 40000, 'hardware')
tom = Manager(name='Tom Doe', age=50, pay=50000)

db = shelve.open('class-shelve')
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db.close()

db = shelve.open('class-shelve')
for key in db:
    print(key, '=>\n ', db[key].name, db[key].pay)
bob = db['bob']
print(bob.last_name())
print(db['tom'].last_name())

# if __name__ == '__main__':
#         print(sue, sue.pay, sue.last_name())
#     for obj in (bob, sue, tom):
#         obj.give_raise(.10)  # вызовет метод give_raise объекта obj
#     print(obj)
    
    
    # bob = Person('Bob Smith', 42, 30000, 'software')
    # sue = Person('Sue Jones', 45, 40000, 'hardware')
    # print(bob.name, sue.pay)
    # print(bob.last_name())
    # sue.give_raise(.10)
    # print(sue.pay)
    
    # tom = Manager(name='Tom Doe', age = 50, pay = 50000)
    # print(tom.last_name())
    # tom.give_raise(.20)
    # print(tom.pay)


# tk = tkinter.Tk()
# frame = tkinter.Frame(tk, relief='ridge', borderwidth=2)
# frame.pack(fill='both', expand=1)
# label = tkinter.Label(frame, text="Hello, World")
# label.pack(fill='x', expand=1)
# button = tkinter.Button(frame, text="Exit", command=tk.destroy)
# button.pack(side='bottom')
# tk.mainloop()
