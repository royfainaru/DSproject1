import time
from AVLTreeList import AVLTreeList
import random as rand


def create_seq_list(n):
    result = AVLTreeList()
    for i in range(n):
        result.append(i)
    return result


def permute_list(lst: AVLTreeList):
    rand.seed(10)
    return lst.permutation()


def timer(func, *args):
    t1 = time.perf_counter()
    func(*args)
    return time.perf_counter() - t1


lst = create_seq_list(74)
print(timer(permute_list, lst))
