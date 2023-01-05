from AVLTreeList import AVLTreeList
from time import perf_counter
from main import avl_random_insert, array_random_insert, avl_insert_first, array_insert_first
import pandas as pd

n_lst = [1500 * 2 ** i for i in range(1, 11)]


def timer(func, n):
    t1 = perf_counter()
    func(n)
    return perf_counter() - t1


avl_times = []
for n in n_lst:
    avl_times.append(timer(avl_insert_first, n))


list_times = []
for n in n_lst:
    list_times.append(timer(array_insert_first, n))


avl_df = pd.DataFrame(avl_times)
list_df = pd.DataFrame(list_times)

avl_df.to_excel('avl_times_insert_first.xlsx')
list_df.to_excel('list_times_insert_first.xlsx')
