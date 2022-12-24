#username - lb3
#id1      - 206913519
#name1    - Lior Ben Avraham
#id2      - complete info
#name2    - complete info  


"""A class represnting a node in an AVL tree"""

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

	"""returns the size of the tree that is rooted in self
	@type node: AVLNode
	@param node: a node
	@rtype: int
	@returns: the size of the tree that is rooted in self
	"""
	def calculateSize(self):
		s = 1
		if self.right is not None:
			s += self.right.getSize()
		if self.left is not None:
			s += self.left.getSize()
		return s

	"""returns the current height of the node

	@type node: AVLNode
	@param node: a node
	@rtype: int
	@returns: the height of the node
	"""
	def calculateHeight(self):
		h_left = -1
		h_right = -1
		if self.left is not None:
			h_left = self.left.getHeight()
		if self.right is not None:
			h_right = self.right.getHeight()
		maxh = max(h_left, h_right)
		return maxh + 1

	"""returns the rank of the node in the tree that is rooted in self (1 <= rank <= tree size)
	@rtype: int
	@returns: the rank of the node in the tree that is rooted in self
	"""
	def getRank(self):
		if self.left is not None:
			return self.left.getSize() + 1
		return 1

	"""returns the index the node in the tree that is rooted in self (0 <= index < tree size)
	@rtype: int
	@returns: the index of the node in the tree that is rooted in self
	"""
	def getIndex(self):
		r = self.getRank()
		if r is None:
			return - 1
		return r - 1

	"""returns the balance factor of the node
	@rtype: int
	@returns: the balance factor of the node
	"""
	def getBF(self):
		h_left = -1
		h_right = -1
		if self.left:
			h_left = self.left.getHeight()
		if self.right:
			h_right = self.right.getHeight()
		return h_left-h_right


	"""returns the value of the node in that rank in the tree that is rooted in self
	@pre: 1 <= i < self.size
	@rtype: AVLNode
	@returns: the value of the node in that rank in the tree that is rooted in self or None of not found
	time complexity: O(logn)
	"""
	def getValueByRank(self, i):
		r = self.getRank()
		print("getvalbyrank", r, self.value)
		if r == i:
			return self.value
		elif r < i and self.right is not None:
			return self.right.getValueByRank(i - r)
		elif r > i:
			return self.left.getValueByRank(i)
		return None

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
	def setLeft(self, node):
		self.left = node
		if node is not None:
			node.setParent(self)
		self.setSize(self.calculateSize())
		self.setHeight(self.calculateHeight())


	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def setRight(self, node):
		self.right = node
		if node:
			node.setParent(self)
		self.setSize(self.calculateSize())
		self.setHeight(self.calculateHeight())

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
	def setHeight(self, h):
		self.height = h


	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def isRealNode(self):
		return self.getValue() is None

	"""sets size

	@type node: AVLNode
	@param s: int
	"""
	def setSize(self, s):
		self.size = s

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
	def insert(self, i, node):
		# rotations counter
		rotcnt = 0
		r = self.getRank()
		if r == i:
			if self.left is None:
				self.setLeft(node)
			else:
				self.left.insertLast(node)
				newsubroot, rotcnt = self.left.rebalance()
				self.setLeft(newsubroot)

		if r > i:
			# insert to the left if no other nodes
			if not self.left:
				self.setLeft(node)
			else:
				# recursive call insert to the left subtree with the same index
				rotcnt += self.left.insert(i, node)
				t = self.left.rebalance()
				newsubroot = t[0]
				rotcnt += t[1]
				self.setLeft(newsubroot)
		if r < i:
			# insert to the right if no other nodes
			if not self.right:
				self.setRight(node)
			else:
				# recursive call insert to the right subtree with updated relevant index
				rotcnt += self.right.insert(i-r, node)
				t = self.right.rebalance()
				newsubroot = t[0]
				rotcnt += t[1]
				self.setRight(newsubroot)

		# update node fields after the changes
		self.setSize(self.calculateSize())
		self.setHeight(self.calculateHeight())

		# returns total number of rotations
		return rotcnt

	"""helper function for AVLNode insert - inserts as last ranked node of the tree of given root node

	@param node: a node
	@type node: AVLNode
	@rtype: None
	@returns: None
	time complexity: O(logn)
	"""
	def insertLast(self, node):
		if self.right is None:
			self.setRight(node)
			return
		self.right.insertLast(node)
		self.setRight(self.right.rebalance())
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
	def delete(self, d):
		# rotations counter
		rotcnt = 0
		r = self.getRank()
		if r == d:
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
			elif self.right and not self.left:
				# check which side to reconnect to parent
				if self.parent.right is self:
					self.parent.setRight(self.right)
				if self.parent.left is self:
					self.parent.setLeft(self.right)
				self.setRight(None)

			# case 3 only right child - connect parent and child of deleted node
			elif self.left and not self.right:
				# check which side to reconnect to parent
				if self.parent.right is self:
					self.parent.setRight(self.left)
				if self.parent.left is self:
					self.parent.setLeft(self.left)
				self.setLeft(None)

			# both sides have children
			else:
				# find successor value for the deleted node - gets value for first ranked in the right subtree
				sucValue = self.findSuccessorValue()
				# copy successor value from right subtree
				self.setValue(sucValue)
				# recursive delete on right subtree with successor node rank (index + 1) in the given tree (1)
				rotcnt += self.right.delete(1)

		# Walk tree and recursive call delete until reaches the node to be deleted
		if r < d and self.right is not None:
			rotcnt += self.right.delete(d - r)
			if self.right:
				# check for needed rotations
				t = self.right.rebalance()
				# reconnect the tree after possible rotations
				self.setRight(t[0])
				rotcnt += t[1]
		if r > d:
			rotcnt += self.left.delete(d)
			if self.left:
				# check for needed rotations
				t = self.left.rebalance()
				# reconnect the tree after possible rotations
				self.setLeft(t[0])
				rotcnt += t[1]

		# returns total number of rotations
		return rotcnt

	"""restores AVLTree condition by rotations 

	@param node: a node
	@type node: AVLNode
	@rtype: tuple(AVLNode, int)
	tuple of , and number of rotations
	@returns: tuple containing 1) new subtree root (AVLNode)
							   2) the number of rotations done to the tree during the rebalancing process
	time complexity: O(logn)
	"""
	def rebalance(self):
		# rotations counter
		rotcnt = 0
		bf = self.getBF()
		newroot = self

		if bf > 1:
			leftbf = self.left.getBF()
			if leftbf < 0:
				# case of left-right rotate (double)
				rotcnt += 1
				# LEFT ROTATE
				newsubroot = AVLNode.leftRotate(self.left, self.left.right, self.left.right.right)
				self.setLeft(newsubroot)

			# case of single right rotation
			rotcnt += 1
			# RIGHT ROTATE
			newroot = AVLNode.rightRotate(self.left.left, self.left, self)

		if bf < -1:
			rightbf = self.right.getBF()
			if rightbf > 0:
				rotcnt += 2
				# case of right-left rotate (double)
				rotcnt += 2

				# RIGHT ROTATE
				newsubroot = AVLNode.rightRotate(self.right.left.left, self.right.left, self.right)
				self.setRight(newsubroot)

			# case of single left rotation
			rotcnt += 1
			# LEFT ROTATE
			newroot = AVLNode.leftRotate(self, self.right, self.right.right)

		# return tuple of new subtree root, and number of rotations
		return newroot, rotcnt

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

	"""finds the value of the successor node for a given node

	@rtype: int
	@returns: the the value of the successor node for a given node
	time complexity: O(logn)
	"""
	def findSuccessorValue(self):
		return self.right.getValueByRank(1)

	"""helper function for listToArray() - recursivly appends values in tree order to given list
	
	@param lst: lst
	@type lst: list
	@rtype: list
	@returns: array of the list values by order, ot empty array if list is empty
	time complexity: O(logn)
	"""
	def listToArrayHelper(self, lst):
		if self.size == 1:
			lst.append(self.value)
			return lst
		if self.left:
			lst = self.left.listToArrayHelper(lst)

		lst.append(self.value)

		if self.right:
			lst = self.right.listToArrayHelper(lst)

		return lst


##################################################
	# TO BE DELETED - JUST FOR PRINTS
	def dump(self):
		if self.left:
			print("LEFT")
			self.left.dump()
			print("LEFT done")
		print("val", self.value,
			  "size", self.size,
			  "rank", self.getRank(),
			  "BF", self.getBF(),
			  "height", self.height)
		if self.right:
			print("RIGHT")
			self.right.dump()
			print("RIGHT DONE")
##################################################

"""
A class implementing the ADT list, using an AVL tree.
"""

class AVLTreeList(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.size = 0
		self.root = None
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
	def retrieve(self, i):
		if self.empty():
			return None
		return self.root.getValueByRank(i+1)

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
	def insert(self, i, val):
		# create new node to insert to the tree
		newnode = AVLNode(val)

		# case of empty tree
		if self.empty():
			self.root = newnode
			self.size = 1
			return 0

		# get rotation count from hepler function
		rotcnt = self.root.insert(i+1, newnode)

		# check for possible rotations needed after changes and get the returned data tuple
		roottuple = self.root.rebalance()

		# update tree root after possible rotations
		self.root = roottuple[0]
		self.root.setParent(None)

		# update rotation count after possible rotations
		rotcnt += roottuple[1]

		# update tree size after insert
		self.size += 1

		# return total number of rotations
		return rotcnt


	"""deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	time complexity: O(logn)
	"""
	def delete(self, i):
		# cases of empty tree and only root
		if self.empty():
			return 0
		if self.size == 1:
			self.root = None
			self.size = 0
			return 0

		# get rotation count from hepler function
		rotcnt = self.root.delete(i+1)

		# check for possible rotations needed after changes and get the returned data tuple
		print("root balance")
		roottuple = self.root.rebalance()

		# update tree root after possible rotations
		self.root = roottuple[0]
		self.root.setParent(None)

		# update rotation count after possible rotations
		rotcnt += roottuple[1]

		# update tree size after delete
		self.size -= 1

		# return total number of rotations
		return rotcnt


	"""returns the value of the first item in the list

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""
	def first(self):
		if self.empty():
			return None
		return self.retrieve(0)

	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	def last(self):
		if self.empty():
			return None
		return self.retrieve(self.size-1)

	"""returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""
	def listToArray(self):
		# create empty list
		treelist = []
		if self.empty():
			return []
		# call helper function to get list
		return self.root.listToArrayHelper(treelist)

	"""returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""
	def length(self):
		return self.size

	"""sort the info values of the list

	@rtype: list
	@returns: an AVLTreeList where the values are sorted by the info of the original list.
	time complexity: ?????????????
	"""
	def sort(self):
		return None

	"""permute the info values of the list 

	@rtype: list
	@returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
	time complexity: ??????????????
	"""
	def permutation(self):
		return None

	"""concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	time complexity: ??????????????
	"""
	def concat(self, lst):
		return None

	"""searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	time complexity: ??????????????
	"""
	def search(self, val):
		return None


	"""returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""
	def getRoot(self):
		if self.empty():
			return None
		return self.root

