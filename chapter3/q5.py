## CTCI - Stacks and Queues Question 5
## Implement a queue with two stacks

class MyQueue():
	def __init__(self):
		self._pushstack = []
		self._popstack = []
		self._size = 0

	def empty(self):
		if len(self._size) == 0:
			return True
		else:
			return False

	def size(self):
		return self._size

	def push(self,val):
		self._pushstack.append(val)
		self._size += 1

	def pop(self):
		if not self.empty():
			if len(self._popstack) == 0:
				for idx in range(len(self._pushstack)):
					self._popstack.append(self._pushstack.pop())
			val = self._popstack.pop()
			self._size -= 1
			return val
		else:
			return None

	def top(self):
		if not self.empty():
			if len(self._popstack) == 0:
				for idx in range(len(self._pushstack)):
					self._popstack.append(self._pushstack.pop())
			return self._popstack[-1]
		else:
			return None



