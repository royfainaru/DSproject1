from AVLTreeList import AVLTreeList
from insert import create_range_list
import random as rand

# retrieve random values and delete them
for _ in range(200):
    lst = create_range_list(50)
    while not lst.empty():
        i = rand.randint(0, lst.size)
        lst.retrieve(i)
        lst.delete(i)

print('success')
