from AVLTreeList import AVLTreeList
from LinkedList import LinkedList
import random as rand
import time

# t = AVLTreeList.AVLTreeList()
# print(t.insert(0, "val1"))
# print(t.insert(1, "val2"))
# print(t.insert(2, "val3"))
# print(t.insert(3, "val4"))
# print(t.insert(2, "val5"))
# print(t.insert(5, "val6"))
#
# t.root.dump()
#
# l = t.listToArray()
# print(l)
#
# print("DELETE RETURN", t.delete(3))
#
# print("seond time")
# t.root.dump()
#
# l = t.listToArray()
# print(l)
#
# print("DELETE RETURN", t.delete(3))
# print("3 time")
#
# t.root.dump()
#
# print(t.last())
# t2 = AVLTreeList.AVLTreeList()
# print(t2.last())
#
# l = t.listToArray()
# print(l)
#
# t3 = AVLTreeList.AVLTreeList()
# print(t3.insert(0, "val1"))
# print(t3.insert(1, "val2"))
# print(t3.insert(2, "val3"))
# print(t3.insert(3, "val4"))
# print(t3.insert(4, "val5"))
# print(t3.insert(5, "val6"))
# l = t.listToArray()
# print(l)
# print(t3.length())
# lst.append(2)
# lst.insert(0, 1)
# print(lst)
# lst.delete(1)
# print(lst)

# for i in range(10):
#     lst.append(str(i))
# lst.insert(3, 'hello')
# print(lst)
# lst.insert(0, 'hi')
# print(lst)
# perm_lst = lst.permutation()
# print(perm_lst)

ALL_I_VALUES = range(1, 11)


def insert_all_numbers(n):
    all_elements = list(range(n))
    AVL_list = AVLTreeList()
    rotcnt = 0
    while all_elements:
        i = rand.randint(0, len(all_elements) - 1)
        rotcnt += AVL_list.insert(rand.randint(0, AVL_list.size), all_elements[i])
        all_elements.pop(i)
    return rotcnt, AVL_list


def delete_all_elements(AVL_list: AVLTreeList):
    rotcnt = 0
    while not AVL_list.empty():
        rotcnt += AVL_list.delete(rand.randint(0, AVL_list.size))
    return rotcnt


def alternate_insert_delete(AVL_list: AVLTreeList, elements_to_insert: list):
    rotcnt = 0
    while elements_to_insert:
        i = rand.randint(0, len(elements_to_insert) - 1)
        rotcnt += AVL_list.insert(rand.randint(0, AVL_list.size), elements_to_insert[i])
        rotcnt += AVL_list.delete(rand.randint(0, AVL_list.size))
        elements_to_insert.pop(i)
    return rotcnt


def q1():
    for i in ALL_I_VALUES:
        t1 = time.perf_counter()
        rotcnt, lst = insert_all_numbers(1500 * 2 ** i)
        t2 = time.perf_counter()
        print(f"i:{i}, time:{t2 - t1}, rotcnt: {rotcnt}")


def q2():
    for i in ALL_I_VALUES:
        rotcnt, lst = insert_all_numbers(1500 * 2 ** i)
        t1 = time.perf_counter()
        delete_all_elements(lst)
        t2 = time.perf_counter()
        print(f"i: {i}, time: {t2 - t1}, rotcnt: {rotcnt}")


def q3():
    for i in ALL_I_VALUES:
        n = 1500 * i ** 2
        t1 = time.perf_counter()
        rotcnt, lst = insert_all_numbers(n // 2)
        t2 = time.perf_counter()
        more_elements = list(range(n//2, (3*n)//4))
        t3 = time.perf_counter()
        rotcnt += alternate_insert_delete(lst, more_elements)
        t4 = time.perf_counter()
        print(f"i:{i}, time: {(t4 - t3) + (t2 - t1)}, rotcnt: {rotcnt}")


def avl_insert_first(n):
    AVL_list = AVLTreeList()
    for i in range(n):
        AVL_list.insert(0, i)
    return


def linked_list_insert_first(n):
    linked_list = LinkedList()
    for i in range(n):
        linked_list.add_at_start(i)
    return


def array_insert_first(n):
    array = []
    for i in range(n):
        array.insert(0, i)
    return


def avl_random_insert(n):
    insert_all_numbers(n)


def linked_list_random_insert(n):
    all_elements = list(range(n))
    linked_list = LinkedList()
    while all_elements:
        i = rand.randint(0, len(all_elements) - 1)
        linked_list.insert(rand.randint(0, linked_list.size), all_elements[i])
        all_elements.pop(i)


def array_random_insert(n):
    all_elements = list(range(n))
    array = []
    while all_elements:
        i = rand.randint(0, len(all_elements) - 1)
        array.insert(rand.randint(0, len(array)), all_elements[i])
        all_elements.pop(i)


def avl_insert_last(n):
    AVL_list = AVLTreeList()
    for i in range(n):
        AVL_list.append(i)


def linked_list_insert_last(n):
    linked_list = LinkedList()
    for i in range(n):
        linked_list.append(i)


def array_insert_last(n):
    array = []
    for i in range(n):
        array.append(i)


def timer(func, i):
    n = 1500 * i
    t1 = time.perf_counter()
    func(n)
    t2 = time.perf_counter()
    return f"i: {i}, n: {n}, time: {t2 - t1}"


funcs = [[avl_insert_first, linked_list_insert_first, array_insert_first], [avl_random_insert, linked_list_random_insert, array_random_insert], [avl_insert_last, linked_list_insert_last, array_insert_last]]

for insertion_position in funcs:
    for func in insertion_position:
        for i in range(1, 11):
            print(timer(func, i))
