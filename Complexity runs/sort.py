# import pandas as pd
#
# from perm import timer, n_lst
# from AVLTreeList import AVLTreeList
#
#
# results = []
# for n in n_lst:
#     lst = AVLTreeList()
#     for i in range(n):
#         lst.append(i)
#     lst = lst.permutation()
#     t = timer(AVLTreeList.sort, lst)
#     results.append({'func': 'sort', 'n': n, 'time': t})
#
# df = pd.DataFrame(results)
# df.to_excel('sort runs.xlsx')
