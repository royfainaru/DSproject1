class Node:
    def __init__(self, key):
        self._key = key
        self._left = None
        self._right = None
        self._parent = None

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        if self.parent or self.left or self.right:
            raise NotImplementedError
        self._key = key

    @property
    def left(self):
        return Node('hello')

    @left.setter
    def left(self, node):
        if self.left:
            self.left.parent = None
        self._left = node
        node.parent = self

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        if self.right:
            self.right.parent = None
        self._right = node
        node.parent = self

    @property
    def parent(self):
        return self._parent

    def isRoot(self) -> bool:
        return self.parent

    def hasChildren(self) -> bool:
        return self.left or self.right

    def successor(self):
        if self.right:
            return BinaryTree(self.right).getMinNode()
        p = self
        if p.isRoot:
            raise OverflowError
        while p.parent.right == self:
            p = p.parent
        if p.isRoot:
            raise OverflowError
        return p.parent

    def predecessor(self):
        if self.left:
            return BinaryTree(self.left).getMaxNode()
        p = self
        if p.isRoot:
            raise OverflowError
        while p.parent.left == self:
            p = p.parent
        if p.isRoot:
            raise OverflowError
        return p.parent


class BinaryTree:
    def __init__(self, root: Node = None):
        self._root = root

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, node):
        self._root = node

    def __bool__(self):
        return self.root

    def getMinNode(self) -> Node | None:
        if not self:
            return
        p = self.root
        while p.left:
            p = p.left
        return p

    def getMaxNode(self) -> Node | None:
        if not self:
            return
        p = self.root
        while p.right:
            p = p.right
        return p

    def __iter__(self):
        return BinaryTreeIterator(self)

    def __getitem__(self, item):
        i = 0
        for p in self:
            if i == item:
                return p.value


class BinaryTreeIterator:
    def __init__(self, tree: BinaryTree):
        self.curr = tree.getMinNode()

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.curr = self.curr.successor()
            return self.curr.value
        except OverflowError:
            raise StopIteration
