import random

# from bubble_sort import sort
# from insert_sort import sort
from select_sort import sort

ok = True
for i in range(100):
    datas = [random.randint(1, 100) for _ in range(20)]
    if list(sorted(datas)) != sort(datas):
        ok = False

print(f'After = Before: {ok}')
