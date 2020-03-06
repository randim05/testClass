# EOFError
# print(help(Exception))

# a = object()
# print(a)
# print(help(a))

try:
    i = input("input something -->")
except:
    print("same error")
else:
    print("no error. you enther - {}".format(i))
