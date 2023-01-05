import time
from AVLTreeList import AVLTreeList
from insert import create_range_list
import random as rand

def permute_list(lst: AVLTreeList):
    rand.seed(8)
    return lst.permutation()


def timer(func, *args):
    t1 = time.perf_counter()
    func(*args)
    return time.perf_counter() - t1


lst = create_range_list(150)
print(timer(permute_list, lst))
