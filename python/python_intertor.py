# -*- encoding: utf-8 -*-

from collections import Iterable
from collections import Iterator


# 可以直接作用于for循环的对象统称为可迭代对象(iterable)
iterable_list = range(10)
print [x ** 2 for x in iterable_list]

# 可迭代对象不可以直接使用next
try:
    next(iterable_list)
except TypeError:
    print 'Next Error'

# 可以被next()函数调用并不断返回下一个值的对象成为迭代器(iterator)
iterator_list = iter(iterable_list)
print next(iterator_list)

print '-----------isinstance----------------'
print 'iterator', isinstance(iterator_list, Iterator)
print 'iterable', isinstance(iterable_list, Iterable)


class MyIterator(object):
    def __init__(self, start=0, end=10, step=1):
        self.start = start
        self.end = end
        self.step = step

    # 被next函数调用的时候使用?
    def __next__(self):
        print 'function call: __next__'
        if self.start >= self.end:
            raise StopIteration('Out Of Index')
        self.start += self.step

        return self.start

    # 被iter函数调用的时候使用，期望返回一个迭代器对象
    def __iter__(self):
        print 'function call: __iter__'
        return iter(range(self.start, self.end))

myIterator = MyIterator(start=0, end=10)

print next(iter(myIterator))

# 会先调用类的__iter__函数，然后对返回的值调用next函数
for x in myIterator:
    print x,

iterable_list = range(10)
# 一个迭代器对象是一次性消耗品，一次循环后就消失殆尽了
iterator_list = iter(iterable_list)

print '\n---------copy_iterator_list----------'
copy_iterator_list = iterator_list
for i in iterator_list:
    print i,
