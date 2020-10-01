# EOFError
# print(help(Exception))

# a = object()
# print(a)
# print(help(a))


# try:
#     i = input("input something -->")
# except:
#     print("same error")
# else:
#     print("no error. you enther - {}".format(i))


class myERROR(Exception):
    def __init__(self, l, a):
        Exception.__init__(self)
        self.l = l
        self.a = a

try:
    i = input("Input same ")
    if len(i) < 3:
        raise myERROR(len(i), 3)
except EOFError:
    print("IO error")
except myERROR as ex:
    print(('ShortInputException: The input was ' +
           '{0} long, expected at least {1}')
          .format(ex.l, ex.a))
else:
    print("input correct")

