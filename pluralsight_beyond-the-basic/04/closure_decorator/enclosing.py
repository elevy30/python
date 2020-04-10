message = 'global'


# def enclosing():
#     message = 'enclosing'
#
#     def local():
#         nonlocal no_such_name
#         message = 'local'
#
#     print('enclosing message:', message)
#     local()
#     print('enclosing message:', message)
#
#
# print('global message:', message)
# enclosing()
# print('global message:', message)


def closure_test():
    x = 'close_over'
    print(closure_test)

    def local_func():
        print(local_func)
        print(x)
    return local_func


lf = closure_test()
lf()
print(lf.__closure__)
