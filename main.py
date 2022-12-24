import AVLTreeList

t = AVLTreeList.AVLTreeList()
print(t.insert(0, "val1"))
print(t.insert(1, "val2"))
print(t.insert(2, "val3"))
print(t.insert(3, "val4"))
print(t.insert(2, "val5"))
print(t.insert(5, "val6"))

t.root.dump()

l = t.listToArray()
print(l)

print("DELETE RETURN", t.delete(3))

print("seond time")
t.root.dump()

l = t.listToArray()
print(l)

print("DELETE RETURN", t.delete(3))
print("3 time")

t.root.dump()

print(t.last())
t2 = AVLTreeList.AVLTreeList()
print(t2.last())

l = t.listToArray()
print(l)

t3 = AVLTreeList.AVLTreeList()
print(t3.insert(0, "val1"))
print(t3.insert(1, "val2"))
print(t3.insert(2, "val3"))
print(t3.insert(3, "val4"))
print(t3.insert(4, "val5"))
print(t3.insert(5, "val6"))
l = t.listToArray()
print(l)
print(t3.length())
