## CTCI - Stacks and Queues Question 6
## Implement a stack where items are in ascending order

class MySortedStack():
	def __init__(self):
		self._stack = []
		self._size = 0

	def empty(self):
		if len(self._size) == 0:
			return True
		else:
			return False

	def size(self):
		return self._size

	def push(self,val):
		self._stack.append(val)
		self._size += 1
		self._sortStack()

	def pop(self):
		if not self.empty():
			val = self._stack.pop()
			self._size -= 1
			return val
		else:
			return None

	def top(self):
		if not self.empty():
			return self._stack[-1]
		else:
			return None

	def _sortStack(self):
		helperStack = []
		while len(self._stack) > 0:
			if len(helperStack) == 0:
				helperStack.append(self._stack.pop())
			else:
				val = self._stack.pop()
				while len(helperStack) > 0 and val > helperStack[-1]:
					self._stack.append(helperStack.pop())
				helperStack.append(val)
		while len(helperStack) > 0:
			self._stack.append(helperStack.pop())

	def printStack(self):
		print self._stack

'''
s = MySortedStack()
s.push(10)
s.push(9)
s.push(8)
s.push(1)
s.push(6)
s.push(4)
s.printStack()
'''


