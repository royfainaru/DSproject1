from AVLTreeList import AVLTreeList
from LinkedList import LinkedList
import random as rand
import time
import pandas as pd

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


def insert_all_numbers(n) -> tuple[int, AVLTreeList]:
    all_elements = list(range(n))
    AVL_list = AVLTreeList()
    rotcnt = 0
    while all_elements:
        i = rand.randint(0, len(all_elements) - 1)
        rotcnt += AVL_list.insert(rand.randint(0, AVL_list.size), all_elements[i])
        all_elements.pop(i)
    return rotcnt, AVL_list


def delete_all_elements(AVL_list: AVLTreeList) -> int:
    rotcnt = 0
    while not AVL_list.empty():
        rotcnt += AVL_list.delete(rand.randint(0, AVL_list.size))
    return rotcnt


def alternate_insert_delete(AVL_list: AVLTreeList, elements_to_insert: list) -> int:
    rotcnt = 0
    while elements_to_insert:
        i = rand.randint(0, len(elements_to_insert) - 1)
        rotcnt += AVL_list.insert(rand.randint(0, AVL_list.size), elements_to_insert[i])
        rotcnt += AVL_list.delete(rand.randint(0, AVL_list.size))
        elements_to_insert.pop(i)
    return rotcnt


def q11():
    results = []
    for i in ALL_I_VALUES:
        n = 1500 * 2 ** i
        t1 = time.perf_counter()
        rotcnt, lst = insert_all_numbers(n)
        t2 = time.perf_counter()
        results.append({'q': '1.1', 'i': i, 'n': n, 'rotations': rotcnt, 'time': t2 - t1})
        print(f'q11, i: {i}')
    return results

def q12():
    results = []
    for i in ALL_I_VALUES:
        n = 1500 * 2 ** i
        rotcnt, lst = insert_all_numbers(n)
        t1 = time.perf_counter()
        delete_all_elements(lst)
        t2 = time.perf_counter()
        results.append({'q': '1.2', 'i': i, 'n': n, 'rotations': rotcnt, 'time': t2 - t1})
        print(f'q12, i: {i}')
    return results


def q13():
    results = []
    for i in ALL_I_VALUES:
        n = 1500 * i ** 2
        t1 = time.perf_counter()
        rotcnt, lst = insert_all_numbers(n // 2)
        t2 = time.perf_counter()
        more_elements = list(range(n//2, (3*n)//4))
        t3 = time.perf_counter()
        rotcnt += alternate_insert_delete(lst, more_elements)
        t4 = time.perf_counter()
        results.append({'q': '1.3', 'i': i, 'n': n, 'rotations': rotcnt, 'time': (t4 - t3) + (t2 - t1)})
        print(f'q13, i: {i}')
    return results


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
    return {'q': '2', 'insertion place': '', 'list ds': '', 'i': i, 'n': n, 'time': t2 - t1, 'avg time': (t2 - t1) / n}


def q1():
    results = []
    for func in [q11, q12, q13]:
        results += func()
    return results


def q2_all_insert_first():
    insertion_place = 'first'
    results = []
    for i in ALL_I_VALUES:
        result = timer(avl_insert_first, i)
        result['insertion place'] = insertion_place
        result['list ds'] = 'avl'
        results.append(result)

        result = timer(linked_list_insert_first, i)
        result['insertion place'] = insertion_place
        result['list ds'] = 'linked'
        results.append(result)

        result = timer(array_insert_first, i)
        result['insertion place'] = insertion_place
        result['list ds'] = 'array'
        results.append(result)
    return results


def q2_all_insert_rand():
    insertion_place = 'random'
    results = []
    for i in ALL_I_VALUES:
        result = timer(avl_random_insert, i)
        result['insertion place'] = insertion_place
        result['list ds'] = 'avl'
        results.append(result)

        result = timer(linked_list_random_insert, i)
        result['insertion place'] = insertion_place
        result['list ds'] = 'linked'
        results.append(result)

        result = timer(array_random_insert, i)
        result['insertion place'] = insertion_place
        result['list ds'] = 'array'
        results.append(result)
    return results


def q2_all_insert_last():
    insertion_place = 'last'
    results = []
    for i in ALL_I_VALUES:
        result = timer(avl_insert_last, i)
        result['insertion place'] = insertion_place
        result['list ds'] = 'avl'
        results.append(result)

        result = timer(linked_list_insert_last, i)
        result['insertion place'] = insertion_place
        result['list ds'] = 'linked'
        results.append(result)

        result = timer(array_insert_last, i)
        result['insertion place'] = insertion_place
        result['list ds'] = 'array'
        results.append(result)
    return results


def q2():
    results = []
    results += q2_all_insert_first()
    results += q2_all_insert_rand()
    results += q2_all_insert_last()
    return results


def export(filename, dict_list):
    df = pd.DataFrame(dict_list)

    df.to_excel(f'{filename}.xlsx', index=False)


export('test after delete root fix', q1())
