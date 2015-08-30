# -*- encoding: utf-8 -*-

# 使用threading的local来对每个进程的私有数据
import threading
import random

local_data = threading.local()


def worker(data):
    show_value(data)
    data.value = random.randint(1, 100)
    show_value(data)


def show_value(data):
    try:
        value = data.value
    except AttributeError:
        print 'No Find Value %s' % threading.currentThread().getName()
    else:
        print 'value: %s' % value

t1 = threading.Thread(target=worker, args=(local_data, ))
t2 = threading.Thread(target=worker, args=(local_data, ))

t1.start()
t2.start()

t1.join()
t2.join()

show_value(local_data)
