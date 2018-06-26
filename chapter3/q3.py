## CTCI - Stacks and Queues Question 3
## Stacks of Plates (Set of Stacks) Not Implemented: popAt()

class SetofStacks():
	def __init__(self):
		self._stackset = []
		self._size = []
		self._cap = 10

	def empty(self):
		if len(self._size) == 0:
			return True
		else:
			return False

	def size(self):
		return sum(self._size)

	def push(self,val):
		if self.empty():
			self._stackset.append([])
			self._size.append(0)
		if self._size[-1] == self._cap:
			self._stackset.append([])
			self._size.append(0)
		self._stackset[-1].append(val)
		self._size[-1] += 1

	def pop(self):
		if not self.empty():
			val = self._stackset[-1].pop()
			self._size[-1] -= 1
			if self._size[-1] == 0:
				self._stackset.pop()
				self._size.pop()
			return val
		else:
			return None

	def top(self):
		if not self.empty():
			return (self._stackset[-1])[-1]
		else:
			return None

	def printStacks(self):
		for s in range(len(self._stackset)):
			print "Stack " + str(s) +":"
			print self._stackset[s]


ss = SetofStacks()
for val in range(0,25):
	ss.push(val)
ss.printStacks()
for val in range(0,25):
	ss.pop()
ss.printStacks()

