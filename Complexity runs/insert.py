from AVLTreeList import AVLTreeList


def create_range_list(n):
    result = AVLTreeList()
    for i in range(n):
        result.append(i)
    return result
