## Basic Singly Linked List Implementation

class Node:
	def __init__(self,value):
		self.val = value
		self.next = None

class LinkedList:
	def __init__(self):
		self._head = None
		self._size = 0

	def size(self):
		return self._size

	def get(self,index):
		if not isinstance(index, (int, long)):
			raise TypeError
		if index<0 or index >= self._size:
			raise IndexError
		curr = self._head
		for idx in range(self._size):
			if idx == index:
				return curr.val
			else:
				curr = curr.next

	def append(self,value):
		if self._head is None:
			n = Node(value)
			self._head = n
			self._size = 1
		else:
			n = Node(value)
			tmp = self._head
			while tmp.next:
				tmp = tmp.next
			tmp.next = n
			self._size += 1

	def insert(self,val,index):
		if not isinstance(index, (int, long)):
			raise TypeError
		if index<0 or index > self._size:
			raise IndexError

		if index == self._size:
			self.append(val)	
		elif index == 0:
			n = Node(val)
			n.next = self._head
			self._head = n
			self._size += 1
		else:
			curr = self._head
			for idx in range(self._size):	
				if idx == index-1:
					n = Node(val)
					tmp = curr.next
					curr.next = n
					n.next = tmp
					self._size += 1
				else:
					curr = curr.next


	def remove(self,index):
		if not isinstance(index, (int, long)):
			raise TypeError
		if index<0 or index >= self._size:
			raise IndexError
	
		if index == 0:
			self._head = self._head.next
			self._size -= 1
		else:
			curr = self._head
			for idx in range(self._size):	
				if idx == index-1:
					tmp = curr.next
					curr.next = tmp.next
					self._size -= 1
				else:
					curr = curr.next

	def getHeadNode(self):
		return self._head

	def printList(self):
		curr = self._head
		s = ""
		while curr:
			s = s + str(curr.val) + " "
			curr = curr.next
		print s


