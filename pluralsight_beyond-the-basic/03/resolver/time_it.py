# in order to measure the cache usage and how it improve the time call, we can use timeit function
# cd resolver
# python -m time_it
from timeit import timeit

from resolver import Resolver

resolve = Resolver()
print(timeit(setup="from __main__ import resolve", stmt="resolve('python.org')", number=1))
print(timeit(setup="from __main__ import resolve", stmt="resolve('python.org')", number=1))

print("{:f}".format(timeit(setup="from __main__ import resolve", stmt="resolve('python.org')", number=1)))

print("{:f}".format(timeit(setup="from __main__ import resolve", stmt="resolve('python.org')", number=1)))