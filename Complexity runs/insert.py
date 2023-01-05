from AVLTreeList import AVLTreeList
from time import perf_counter
from main import avl_random_insert, array_random_insert
import pandas as pd

n_lst = [1500 * 2 ** i for i in range(1, 11)]


def timer(func, n):
    t1 = perf_counter()
    func(n)
    return perf_counter() - t1


avl_times = []
for n in n_lst:
    avl_times.append(timer(avl_random_insert, n))


list_times = []
for n in n_lst:
    list_times.append(timer(array_random_insert, n))


avl_df = pd.DataFrame(avl_times)
list_df = pd.DataFrame(list_times)
