## CTCI - Stacks and Queues Question 2
## Stack with a min function that runs in O(1)

class MinStack():
	def __init__(self):
		self._stack = []
		self._size = 0
		self._minVal = []

	def empty(self):
		if self._size == 0:
			return True
		else:
			return False

	def size(self):
		return self._size

	def push(self,val):
		self._stack.append(val)
		self._size += 1
		if len(self._minVal) == 0:
			self._minVal.append(val)
		else:
			if val<=self._minVal[-1]:
				self._minVal.append(val)

	def pop(self):
		if not self.empty():
			val = self._stack.pop()
			self._size -= 1
			if val==self._minVal[-1]:
				self._minVal.pop()
			return val
		else:
			return None

	def top(self):
		if not self.empty():
			return self._stack[-1]
		else:
			return None

	def min(self):
		if not self.empty():
			return self._minVal[-1]
		else:
			return None	


'''
s = MinStack()
s.push(4)
s.push(5)
s.push(6)
s.push(7)
s.push(3)
s.push(1)
s.push(2)
print s.min()
s.pop()
print s.min()
s.pop()
print s.min()
s.pop()
print s.min()
'''
