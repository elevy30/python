import socket


class Resolver:

    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]

    def clear(self):
        self._cache.clear()

    def has_host(self, host):
        return host in self._cache

# from resolver.resolver import Resolver
# resolve = Resolver()
# resolve('sixty-north.com')


# in order to measure the cache usage and how it improve the time call, we can use timeit function
# from timeit import timeit
# timeit(setup="from __main__ import resolve", stmt="resolve('python.org')", number=1)
# timeit(setup="from __main__ import resolve", stmt="resolve('python.org')", number=1)
# print("{:f}".format(_))


# from resolver.resolver import Resolver
# Resolver
# resolve = Resolver()
# resolve('sixty-north.com')

