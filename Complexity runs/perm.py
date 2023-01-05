import time
from AVLTreeList import AVLTreeList
import random as rand


def create_seq_list(n):
    result = AVLTreeList()
    for i in range(n):
        result.append(i)
    return result


def permute_list(lst: AVLTreeList):
    return lst.permutation()


def timer(func, *args):
    t1 = time.perf_counter()
    func(*args)
    return time.perf_counter() - t1


lst = create_seq_list(7004)
perm_lst = lst.permutation()
print(lst.length(), lst)
print(perm_lst.length(), perm_lst)

lst.concat(perm_lst)
print(lst.length(), lst)
