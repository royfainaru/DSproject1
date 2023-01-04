# username - lb3
# id1      - 206913519
# name1    - Lior Ben Avraham
# id2      - 207002403
# name2    - Roy Fainaru

import random as rand


"""A class representing a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

	@type value: str
	@param value: data of your node
	"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0
        self.size = 1

    def __bool__(self):
        return self.value is not None

    def __repr__(self):
        return f"{'<' if self.left else ''}{'^' if self.parent else ''}{f'({self.value})'}{'>' if self.right else ''}"

    """returns the size of the tree that is rooted in self
    
	@type node: AVLNode
	@param node: a node
	@rtype: int
	@returns: the size of the tree that is rooted in self
	"""

    def calculateSize(self):
        """
        Calculate the size of the binary tree.

        Time complexity: O(1)
        This is because the method has a precondition that the size attributes of the left and right children
        are already updated.

        Returns:
            int: The size of the binary tree.
        """
        size = 1  # initialize size to 1 for the current node
        if self.right:
            size += self.right.getSize()  # add size of right subtree
        if self.left:
            size += self.left.getSize()  # add size of left subtree
        return size

    """returns the current height of the node

	@type node: AVLNode
	@param node: a node
	@rtype: int
	@returns: the height of the node
	"""
    def calculateHeight(self):
        left_height = -1  # initialize left height to -1
        right_height = -1  # initialize right height to -1
        if self.left:
            left_height = self.left.getHeight()  # get left height
        if self.right:
            right_height = self.right.getHeight()  # get right height
        return max(left_height, right_height) + 1  # return the maximum of the left and right heights, plus 1

    """returns the rank of the node in the tree that is rooted in self (1 <= rank <= tree size)
    
	@rtype: int
	@returns: the rank of the node in the tree that is rooted in self
	"""
    def getRank(self):
        if self.left:  # if there is a left child
            return self.left.getSize() + 1  # return the size of the left subtree, plus 1 for the current node
        # if there is no left child, return 1 for the current node if it's not virtual, 0 otherwise
        return 1 if self else 0

    """returns the index the node in the tree that is rooted in self (0 <= index < tree size)
	@rtype: int
	@returns: the index of the node in the tree that is rooted in self
	"""
    def getIndex(self):
        return self.getRank() - 1

    """returns the balance factor of the node
    
	@rtype: int
	@returns: the balance factor of the node
	"""
    def getBF(self):
        left_height = -1  # initialize left height to -1
        right_height = -1  # initialize right height to -1
        if self.left:
            left_height = self.left.getHeight()  # get left height
        if self.right:
            right_height = self.right.getHeight()  # get right height
        return left_height - right_height  # return the difference between the left and right heights

    """returns the value of the node in that rank in the tree that is rooted in self
    
	@pre: 1 <= i < self.size
	@rtype: AVLNode
	@returns: the value of the node in that rank in the tree that is rooted in self or None of not found
	time complexity: O(logn)
	"""
    def getValueByRank(self, rank):
        """
        Get the value of the node with the specified rank in the binary tree.

        Time complexity: O(log(n)), where n is the number of nodes in the binary tree.
        This is because the method must travel downwards in the tree in order to find the node with the given value.
        Args:
            rank (int): The rank of the node to find.

        Returns:
            Any: The value of the node with the specified rank, or None if no such node exists.
        """
        if self.getRank() == rank:  # if the current node has the specified rank
            return self.value  # return the value of the current node
        elif self.getRank() < rank and self.right:  # if the rank is greater than the current rank and there is a right child
            return self.right.getValueByRank(rank - self.getRank())  # recursively search the right subtree
        elif self.getRank() > rank:  # if the rank is less than the current rank
            return self.left.getValueByRank(rank)  # recursively search the left subtree
        return None  # if no node with the specified rank was found, return None

    """returns the left child
    
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	"""
    def getLeft(self):
        return self.left

    """returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	"""
    def getRight(self):
        return self.right

    """returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
    def getParent(self):
        return self.parent

    """return the value

	@rtype: str
	@returns: the value of self, None if the node is virtual
	"""
    def getValue(self):
        return self.value

    """returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
    def getHeight(self):
        return self.height

    """sets left child

	@type node: AVLNode
	@param node: a node
	"""
    # Set the left child of the node
    # Also update the size and height attributes of the node
    def setLeft(self, node):
        self.left = node  # set the left child
        if node:  # if a node was provided
            node.setParent(self)  # set the parent of the node to the current node
        self.setSize(self.calculateSize())  # update the size attribute
        self.setHeight(self.calculateHeight())  # update the height attribute

    """sets right child

	@type node: AVLNode
	@param node: a node
	"""
    # Set the right child of the node
    # Also update the size and height attributes of the node
    def setRight(self, node):
        self.right = node  # set the right child
        if node:  # if a node was provided
            node.setParent(self)  # set the parent of the node to the current node
        self.setSize(self.calculateSize())  # update the size attribute
        self.setHeight(self.calculateHeight())  # update the height attribute

    """sets parent

	@type node: AVLNode
	@param node: a node
	"""
    def setParent(self, node):
        self.parent = node

    """sets value

	@type value: str
	@param value: data
	"""
    def setValue(self, value):
        self.value = value

    """sets the height of the node

	@type h: int
	@param h: the height
	"""
    def setHeight(self, height):
        self.height = height

    """returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
    def isRealNode(self):
        return self

    """sets size

	@type node: AVLNode
	@param s: int
	"""
    def setSize(self, size):
        self.size = size

    """returns the size of the tree rooted in the node

	@type node: AVLNode
	@rtype : int
	@returns: the size of tree rooted in the node
	"""
    def getSize(self):
        return self.size

    """helper function for AVLTreeList insert

	@param i: list index
	@param node: a node
	@type i: int
	@type node: AVLNode
	@rtype: int
	@returns: the number of rotations done to the tree during the insert process
	time complexity: O(logn)
	"""
    def insert(self, rank, node):
        """
            Insert a node into the AVL tree at the specified rank.

            Time complexity: O(logn), where n is the number of nodes in the AVL tree.
            This is because the method must perform a logarithmic number of rotations in the worst case.

            Args:
                rank (int): The rank at which to insert the new node.
                node (Node): The node to insert.

            Returns:
                int: The total number of rotations performed during the insertion.
            """

        # rotations counter
        rotations_count = 0
        if self.getRank() == rank:
            if not self.left:
                self.setLeft(node)
            else:
                self.left.insertLast(node)
                new_sub_root, rotations_count = self.left.rebalance()
                self.setLeft(new_sub_root)

        elif self.getRank() > rank:
            # insert to the left if no other nodes
            if not self.left:
                self.setLeft(node)
            else:
                # recursive call insert to the left subtree with the same index
                rotations_count += self.left.insert(rank, node)
                new_sub_root, tmp_rot_cnt = self.left.rebalance()
                rotations_count += tmp_rot_cnt
                self.setLeft(new_sub_root)

        elif self.getRank() < rank:
            # insert to the right if no other nodes
            if not self.right:
                self.setRight(node)
            else:
                # recursive call insert to the right subtree with updated relevant index
                rotations_count += self.right.insert(rank - self.getRank(), node)
                new_sub_root, tmp_rot_cnt = self.right.rebalance()
                rotations_count += tmp_rot_cnt
                self.setRight(new_sub_root)

        # update node fields after the changes
        self.setSize(self.calculateSize())
        self.setHeight(self.calculateHeight())

        # returns total number of rotations
        return rotations_count

    """helper function for AVLNode insert - inserts as last ranked node of the tree of given root node

	@param node: a node
	@type node: AVLNode
	@rtype: None
	@returns: None
	time complexity: O(logn)
	"""
    def insertLast(self, node):
        if not self.right:
            self.setRight(node)
            return

        self.right.insertLast(node)
        self.setRight(self.right.rebalance()[0])

        self.setSize(self.calculateSize())
        self.setHeight(self.calculateHeight())

    """helper function for AVLTreeList delete

	@param d: list index
	@param node: a node
	@type d: int
	@type node: AVLNode
	@rtype: int
	@returns: the number of rotations done to the tree during the delete process
	time complexity: O(logn)
	"""
    def delete(self, rank):
        """
            Delete the node with the specified rank from the AVL tree.

            Time complexity: O(logn), where n is the number of nodes in the AVL tree.
            This is because the method must perform a logarithmic number of rotations in the worst case.

            Args:
                rank (int): The rank of the node to delete.

            Returns:
                int: The total number of rotations performed during the deletion.
            """

        # rotations counter
        rotations_count = 0
        if self.getRank() == rank:
            # delete this node - depends on the case
            # case 1 no children - leaf can be deleted simply
            if not self.right and not self.left:
                if self.parent:
                    # check which side to reconnect to parent
                    if self.parent.right is self:
                        self.parent.setRight(None)
                    if self.parent.left is self:
                        self.parent.setLeft(None)

            # case 2 only left child - connect parent and child of deleted node
            # NEED TO CHECK IF THERE IS A PARENT TO RECONNECT
            elif self.right and not self.left:
                if self.parent:
                    # check which side to reconnect to parent
                    if self.parent.right is self:
                        self.parent.setRight(self.right)
                    if self.parent.left is self:
                        self.parent.setLeft(self.right)
                self.setRight(None)

            # case 3 only right child - connect parent and child of deleted node
            elif self.left and not self.right:
                if self.parent:
                    # check which side to reconnect to parent
                    if self.parent.right is self:
                        self.parent.setRight(self.left)
                    if self.parent.left is self:
                        self.parent.setLeft(self.left)
                self.setLeft(None)

            # both sides have children
            else:
                # find successor value for the deleted node - gets value for first ranked in the right subtree
                successor_value = self.findSuccessorValue()
                # copy successor value from right subtree
                self.setValue(successor_value)
                # recursive delete on right subtree with successor node rank (index + 1) in the given tree (1)
                rotations_count += self.right.delete(1)

        # Walk tree and recursive call delete until reaches the node to be deleted
        if self.getRank() < rank and self.right:
            rotations_count += self.right.delete(rank - self.getRank())
            if self.right:
                # check for needed rotations
                new_sub_root, tmp_rot_cnt = self.right.rebalance()
                # reconnect the tree after possible rotations
                self.setRight(new_sub_root)
                rotations_count += tmp_rot_cnt
        if self.getRank() > rank:
            rotations_count += self.left.delete(rank)
            if self.left:
                # check for needed rotations
                new_sub_root, tmp_rot_cnt = self.left.rebalance()
                # reconnect the tree after possible rotations
                self.setLeft(new_sub_root)
                rotations_count += tmp_rot_cnt

        # returns total number of rotations
        return rotations_count

    """restores AVLTree condition by rotations 

	@param node: a node
	@type node: AVLNode
	@rtype: tuple(AVLNode, int)
	tuple of , and number of rotations
	@returns: tuple containing 1) new subtree root (AVLNode)
							   2) the number of rotations done to the tree during the rebalancing process
	time complexity: O(1)
	"""

    def rebalance(self):
        """
        Rebalance the AVL tree if necessary after an insertion or deletion.

        Time complexity: O(1), since the method performs a constant number of operations.

        Returns:
            tuple: A tuple containing the new root of the balanced subtree, and the number of rotations performed.
        """
        # rotations counter
        rotations_count = 0
        balance_factor = self.getBF()  # get the balance factor of the current node
        new_root = self  # the new root of the balanced subtree is initially set to the current node

        if balance_factor > 1:  # if the balance factor is positive
            left_bf = self.left.getBF()  # get the balance factor of the left child
            if left_bf < 0:
                # case of left-right rotate (double)
                rotations_count += 1
                # LEFT ROTATE
                new_sub_root = AVLNode.leftRotate(self.left, self.left.right, self.left.right.right)
                self.setLeft(new_sub_root)
            # case of single right rotation
            rotations_count += 1
            # RIGHT ROTATE
            new_root = AVLNode.rightRotate(self.left.left, self.left, self)

        if balance_factor < -1:  # if the balance factor is negative
            right_bf = self.right.getBF()  # get the balance factor of the right child
            if right_bf > 0:
                # case of right-left rotate (double)
                rotations_count += 1
                # RIGHT ROTATE
                new_sub_root = AVLNode.rightRotate(self.right.left.left, self.right.left, self.right)
                self.setRight(new_sub_root)
            # case of single left rotation
            rotations_count += 1
            # LEFT ROTATE
            new_root = AVLNode.leftRotate(self, self.right, self.right.right)

        # return tuple of new subtree root, and number of rotations
        return new_root, rotations_count

    """rotates left three given nodes (could be virtual) to a balanced subtree

	@param a: a node
	@param b: a node
	@param c: a node
	@type a: AVLNode
	@type b: AVLNode
	@type c: AVLNode
	@rtype: AVLNode
	@returns: the node object that is the new balanced subtree root
	"""
    def leftRotate(a, b, c):
        # The new subtree root will be b
        a.setRight(b.left)

        # Update data a
        a.setSize(a.calculateSize())
        a.setHeight(a.calculateHeight())

        # Connect a to b
        b.setLeft(a)
        return b

    """rotates right three given nodes (could be virtual) to a balanced subtree

	@param a: a node
	@param b: a node
	@param c: a node
	@type a: AVLNode
	@type b: AVLNode
	@type c: AVLNode
	@rtype: AVLNode
	@returns: the node object that is the new balanced subtree root
	"""
    def rightRotate(a, b, c):
        # The new root will be b
        c.setLeft(b.right)

        # Update data c
        c.setSize(c.calculateSize())
        c.setHeight(c.calculateHeight())

        # Connect c to b
        b.setRight(c)
        return b

    def min(self):
        if not self.left:
            return self

        return self.left.min()

    def max(self):
        if not self.right:
            return self

        return self.right.max()

    def successor(self):
        """
        Find the successor of the current node in the AVL tree.

        Time complexity: O(logn), where n is the size of the tree. In the worst case, this method will traverse the height
                         of the tree in order to find the successor.

        Returns:
            AVLNode: The successor of the current node, or None if there is no successor.
        """
        if self.right:  # if the current node has a right child, the successor is the minimum value in the right subtree
            return self.right.min()

        # otherwise, the successor is the closest ancestor whose left child is also an ancestor of the current node
        p = self
        while p.parent and p.parent.right is p:
            p = p.parent

        return p.parent

    def predecessor(self):
        """
        Find the predecessor of the current node in the AVL tree.

        Time complexity: O(logn), where n is the size of the tree. In the worst case, this method will traverse the height
                         of the tree in order to find the successor.

        Returns:
            AVLNode: The predecessor of the current node, or None if there is no predecessor.
        """
        if self.left:  # if the current node has a left child, the predecessor is the maximum value in the left subtree
            return self.left.max()

        # otherwise, the predecessor is the closest ancestor whose right child is also an ancestor of the current node
        p = self
        while p.parent and p.parent.left is p:
            p = p.parent

        return p.parent

    """finds the value of the successor node for a given node

	@rtype: int
	@returns: the the value of the successor node for a given node
	time complexity: O(logn)
	"""
    # PROBLEMO
    def findSuccessorValue(self):
        return self.right.getValueByRank(1)

    """helper function for listToArray() - recursivly appends values in tree order to given list

	@param lst: lst
	@type lst: list
	@rtype: list
	@returns: array of the list values by order, ot empty array if list is empty
	time complexity: O(n)
	"""
    def listToArrayHelper(self, lst):
        """
        Recursive helper function to convert the AVL tree to a sorted list.

        Time complexity: O(n), where n is the number of nodes in the tree. This method will traverse every node in the tree
                         in order to add its value to the list.

        Args:
            lst (list): The list to which the values of the AVL tree will be added.

        Returns:
            list: The list with the values of the AVL tree added in sorted order.
        """
        if self.left:  # if the current node has a left child, add the values of the left subtree to the list
            lst = self.left.listToArrayHelper(lst)

        lst.append(self.value)  # add the value of the current node to the list

        if self.right:  # if the current node has a right child, add the values of the right subtree to the list
            lst = self.right.listToArrayHelper(lst)

        return lst


"""
A class implementing the ADT list, using an AVL tree.
"""


class AVLTreeList(object):
    """
	Constructor, you are allowed to add more fields.

	"""
    def __init__(self):
        self.size = 0
        self.root: AVLNode | None = None

    # add your fields here

    """returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""
    def empty(self):
        return self.size == 0

    """retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	time complexity: O(logn)
	"""
    def retrieve(self, index):
        """
        Retrieve the value at a given index in the AVL tree.

        Time complexity: O(log(n)), where n is the number of nodes in the tree. In the worst case, this method will traverse
                         the logarithm of the number of nodes in the tree in order to find the value at the given index.

        Args:
            index (int): The index of the value to be retrieved.

        Returns:
            any: The value at the given index, or None if the index is out of bounds.
        """
        if self.empty():  # if the tree is empty, return None
            return None
        rank = index + 1  # the rank of the node to be retrieved is the index plus 1
        # retrieve the value at the given rank in the tree
        return self.root.getValueByRank(rank)

    """inserts val at position i in the list

	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	time complexity: O(logn)
	"""
    def insert(self, index, value):
        """
        Insert a value into the AVL tree at a given index.

        Time complexity: O(log(n)), where n is the number of nodes in the tree. In the worst case, this method will traverse
                         the logarithm of the number of nodes in the tree in order to find the correct position for the
                         new value.

        Args:
            index (int): The index at which to insert the value.
            value (any): The value to be inserted into the tree.

        Returns:
            int: The total number of rotations performed during the insert operation.
        """
        # create new node to insert to the tree
        new_node = AVLNode(value)

        # case of empty tree
        if self.empty():
            self.root = new_node
            self.size = 1
            return 0

        # get rotation count from hepler function
        rank = index + 1
        rotations_count = self.root.insert(rank, new_node)

        # check for possible rotations needed after changes and get the returned data tuple
        new_root, tmp_rot_cnt = self.root.rebalance()

        # update tree root after possible rotations
        self.root = new_root
        self.root.setParent(None)

        # update rotation count after possible rotations
        rotations_count += tmp_rot_cnt

        # update tree size after insert
        self.size += 1

        # return total number of rotations
        return rotations_count

    def append(self, val):
        """
        Append a value to the end of the AVL tree.

        Time complexity: O(log(n)), where n is the number of nodes in the tree. In the worst case, this method will traverse
                         the logarithm of the number of nodes in the tree in order to find the correct position for the
                         new value.

        Args:
            val (any): The value to be inserted into the tree.
        """
        return self.insert(self.size, val)

    """deletes the i-th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	time complexity: O(logn)
	"""
    def delete(self, index):
        """
        Delete a value from the AVL tree at a given index.

        Time complexity: O(log(n)), where n is the number of nodes in the tree. In the worst case, this method will traverse
                         the logarithm of the number of nodes in the tree in order to find the correct node to delete,
                         and in the worst case, it also performs rotations to maintain the balance of the AVL tree.
                         The number of rotations performed depends on the balance factor of the nodes and can be at most
                         O(log n).

        Args:
            index (int): The index of the value to be deleted.
        """
        if not 0 <= index < self.size:
            return 0

        # cases of empty tree and only root
        if self.empty():
            return 0
        if self.size == 1:
            self.root = None
            self.size = 0
            return 0

        # get rotation count from hepler function
        rank = index + 1
        rotations_count = self.root.delete(rank)

        # check for possible rotations needed after changes and get the returned data tuple
        new_root, tmp_rot_cnt = self.root.rebalance()

        # update tree root after possible rotations
        self.root = new_root
        self.root.setParent(None)

        # update rotation count after possible rotations
        rotations_count += tmp_rot_cnt

        # update tree size after delete
        self.size -= 1

        # return total number of rotations
        return rotations_count

    """returns the value of the first item in the list

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	time complexity: O(logn)
	"""
    def first(self):
        '''
        time complexity:
        The time complexity of this method is O(log n)
        because it performs a search in the tree to find the first element,
        which is the node with rank 1 in the tree
        '''
        if self.empty():
            return None
        return self.retrieve(0)

    """returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	time complexity: O(logn)
	"""
    def last(self):
        '''
        time complexity:
        The time complexity of this method is O(log n)
        because it performs a search in the tree to find the last element,
        which is the node with rank 'size' in the tree
        '''
        if self.empty():
            return None
        return self.retrieve(self.size - 1)

    """returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	time complexity: O(n)
	"""
    def listToArray(self):
        '''
        This method has a time complexity of O(n)
        because it must traverse through all nodes of the tree in order to create the resulting list.
        '''
        # create empty list
        result = []
        if self.empty():
            return result
        # call helper function to get list
        return self.root.listToArrayHelper(result)

    """returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""
    def length(self):
        return self.size

    '''O(log(n))'''

    def regular_insert(self, node: AVLNode):
        """
        Insert a node into the AVL tree using a regular binary search tree insert method.

        The time complexity of this method is O(log(n)), where n is the number of nodes in the AVL tree.
        This is because the method performs a binary search to find the correct position to insert the
        new node, which has a time complexity of O(log(n)).

        Parameters:
        node (AVLNode): The node to insert into the AVL tree.
        """

        # If the AVL tree is empty, set the root to the new node and set the size to 1
        if self.empty():
            self.root = node
            self.size = 1
            return

        # If the value of the new node is less than or equal to the root, insert it as the left child
        # or recursively insert it into the left subtree
        if node.getValue() <= self.root.getValue():
            if self.root.getLeft():
                left_sub_tree = AVLTreeList()
                left_sub_tree.regular_insert(self.root.getLeft())
                left_sub_tree.regular_insert(node)
            else:
                self.root.setLeft(node)
        # Otherwise, insert the new node as the right child or recursively insert it into the right subtree
        else:
            if self.root.getRight():
                right_sub_tree = AVLTreeList()
                right_sub_tree.regular_insert(self.root.getRight())
                right_sub_tree.regular_insert(node)
            else:
                self.root.setRight(node)

    # The regular_insert sorts the tree
    # upon insertion by node's value.
    # using pre-order traversal of the tree.
    def _sort_rec(self, sorted_tree):
        """
        Recursively sort the AVL tree into a tree list in ascending order.

        The time complexity of this method is O(n log(n)), where n is the number of nodes in the AVL tree.
        This is because the method iterates through every node in the AVL tree once in order to add it
        to the sorted tree list, and each insertion has a time complexity of O(log(n)). Therefore, the
        overall time complexity is O(n * log(n)) = O(n log(n)).

        Parameters:
        sorted_tree (AVLTreeList): The sorted tree list to insert the nodes into.

        Returns:
        AVLTreeList: The sorted tree list with all the nodes from the AVL tree in ascending order.
        """

        # Insert the root of the AVL tree into the sorted tree list
        sorted_tree.regular_insert(AVLNode(self.root.value))

        # If the root has a left child, recursively sort the left subtree and insert it into the sorted tree list
        if self.root.getLeft():
            left_sub_tree = AVLTreeList()
            left_sub_tree.regular_insert(self.root.getLeft())
            sorted_tree = left_sub_tree._sort_rec(sorted_tree)

        # If the root has a right child, recursively sort the right subtree and insert it into the sorted tree list
        if self.root.getRight():
            right_sub_tree = AVLTreeList()
            right_sub_tree.regular_insert(self.root.getRight())
            sorted_tree = right_sub_tree._sort_rec(sorted_tree)

        # Return the sorted tree list
        return sorted_tree

    """sort the info values of the list

	@rtype: list
	@returns: an AVLTreeList where the values are sorted by the info of the original list.
	time complexity: O(n*log(n))
	"""

    def sort(self):
        """
        Sort the AVL tree into a tree list in ascending order.

        The time complexity of this method is O(n log(n)), where n is the number of nodes in the AVL tree.
        This is because the method calls the `_sort_rec` method, which has a time complexity of O(n log(n)).
        The rest of the method has a constant time complexity.

        Returns:
        AVLTreeList: The sorted tree list with all the nodes from the AVL tree in ascending order.
        """

        # Sort the AVL tree into a tree list using the `_sort_rec` method
        tmpBST: AVLTreeList = self._sort_rec(AVLTreeList())

        # Create a new tree list to store the result
        result = AVLTreeList()

        # Set p to the root of the sorted tree list
        p = tmpBST.root

        # Move p to the leftmost node in the sorted tree list
        while p and p.getLeft():
            p = p.getLeft()

        # While p has a successor, add its value to the result tree list and move to the successor
        while p and p.successor():
            result.append(p.value)
            p = p.successor()

        # Add the value of the last node to the result tree list
        result.append(p.value)

        return result

    """permute the info values of the list 

	@rtype: list
	@returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
	time complexity: O(n*log(n))
	"""

    def permutation(self):
        """
        Generate a permutation of the nodes in the AVL tree.

        The time complexity of this method is O(n log(n)), where n is the number of nodes in the AVL tree.
        This is because the method calls the `retrieve` and `delete` methods, which both have a time complexity
        of O(log(n)). The rest of the method has a constant time complexity.

        Returns:
        AVLTreeList: A tree list with the nodes from the AVL tree in a random permutation.
        """

        # Get the size of the AVL tree
        n = self.size

        # Create a list of indices from 0 to n-1
        indices = range(n)

        # Create a new tree list to store the indices
        indices_list = AVLTreeList()

        # Create a new tree list to store the result
        result = AVLTreeList()

        # Add all the indices to the indices tree list
        for i in indices:
            indices_list.append(i)

        # While the indices tree list is not empty, select a random index, retrieve the corresponding node
        # from the AVL tree, and add it to the result tree list. Then delete the index from the indices tree list.
        while not indices_list.empty():
            i = rand.randint(0, indices_list.size - 1)
            random_index = indices_list.retrieve(i)
            result.append(self.retrieve(random_index))
            indices_list.delete(i)

        # Return the result tree list
        return result

    """concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	time complexity: O(k * log(n)) where n = self.size and k = lst.size
	"""

    def concat(self, lst):
        """
        Concatenate the nodes of another tree list to the end of the AVL tree.

        The time complexity of this method is O(k log(n)), where k is the number of nodes in the tree list
        being concatenated. This is because the method calls the `append` method, which has a time complexity
        of O(log(n)). The rest of the method has a constant time complexity.

        Parameters:
        lst (AVLTreeList): The tree list to concatenate to the end of the AVL tree.

        Returns:
        int: The absolute difference in height between the root of the AVL tree and the root of the tree list.
        """

        # Calculate the absolute difference in height between the root of the AVL tree and the root of the tree list
        to_return = abs(self.root.getHeight() - lst.root.getHeight())

        # Set p to the first node of the tree list
        p: AVLNode = lst.first()

        # Set max_p to the last node of the tree list
        max_p = lst.last()

        # While p is not the last node of the tree list, append its value to the AVL tree and move to the successor
        while p != max_p:
            self.append(p.value)
            p = p.successor()

        # Append the value of the last node of the tree list to the AVL tree
        self.append(p.value)

        # Return the absolute difference in height
        return to_return

    """searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	time complexity: O(n)
	"""

    def search(self, val):
        """
        Search for a node with a specific value in the AVL tree.

        The time complexity of this method is O(n), where n is the number of nodes in the AVL tree.
        This is because the method iterates through every node in the AVL tree once in order to find the
        node with the target value.

        Parameters:
        val: The value to search for.

        Returns:
        int: The index of the node with the target value, or -1 if the value is not found.
        """

        # Set p to the first node of the AVL tree
        p: AVLNode = self.first()

        # Set i to 0
        i = 0

        # While p does not have the target value and has a successor, move to the successor and increment i
        while p.value != val and p.successor():
            p = p.successor()
            i += 1

        # If p has the target value, return i. Otherwise, return -1
        if p.value == val:
            return i
        return -1

    """returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""
    def getRoot(self):
        if self.empty():
            return None
        return self.root

    def __repr__(self):
        return self.listToArray().__repr__()

    def __iter__(self):
        return self.listToArray().__iter__()
