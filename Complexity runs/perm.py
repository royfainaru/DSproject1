import time
import pandas as pd
from AVLTreeList import AVLTreeList


def create_seq_list(n):
    result = AVLTreeList()
    for i in range(n):
        result.append(i)
    return result


def timer(func, *args):
    t1 = time.perf_counter()
    func(*args)
    return time.perf_counter() - t1


n_lst = [1500 * 2 ** i for i in range(1, 9)]
results = []
for n in n_lst:
    lst = AVLTreeList()
    for i in range(n):
        lst.append(i)
    t = timer(AVLTreeList.permutation, lst)
    results.append({'func': 'perm', 'n': n, 'time': t})