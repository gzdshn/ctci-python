## CTCI - Stacks and Queues Question 1
## Multiple Stacks in a Single Array

class MultiStack:
	def __init__(self,numStacks):
		self._numStacks = numStacks
		self._perStackCapacity = 10
		self._totalCapacity = self._perStackCapacity * numStacks
		self._stackarray = [None] * self._totalCapacity
		self._stackTop = [None] * numStacks
		self._stackSize = [0] * numStacks

	''' 
	empty(stack) - checks if given stack is empty, returns boolean
	'''
	def empty(self,stack):
		if stack>self._numStacks or stack<=0:
			raise IndexError()
		if self._stackSize[stack-1] == 0:
			return True
		else:
			return False

	''' 
	push(val,stack) - pushes element val to the given stack,
		resizes if stack is already full, returns nothing
	'''
	def push(self,val,stack):
		if stack>self._numStacks or stack<=0:
			raise IndexError()
		stackIdx = stack-1
		# Trigger resize if stack is full
		if self._stackSize[stackIdx] == self._perStackCapacity:
			self.resize()
		# Push the element
		if self.empty(stack):	
			arrayIdx = stackIdx*self._perStackCapacity	
		else:
			arrayIdx = self._stackTop[stackIdx] + 1
		self._stackarray[arrayIdx] = val
		self._stackTop[stackIdx] = arrayIdx
		self._stackSize[stackIdx] += 1

	''' 
	pop(stack) - pops and returns the top element from the given stack,
		if stack is empty, returns None.
	'''
	def pop(self,stack):
		if stack>self._numStacks or stack<=0:
			raise IndexError()
		stackIdx = stack-1
		if not self.empty(stack):
			arrayIdx = self._stackTop[stackIdx]	
			value = self._stackarray[arrayIdx]
			self._stackarray[arrayIdx] = None
			self._stackTop[stackIdx] = arrayIdx - 1
			if self._stackTop[stackIdx] < stackIdx*self._perStackCapacity:
				self._stackTop[stackIdx] = None
			self._stackSize[stackIdx] -= 1
			if self._stackSize[stackIdx] < 0:
				self._stackSize[stackIdx] = 0
			return value
		else:
			return None

	''' 
	top(stack) - returns the top element from the given stack,
		if stack is empty, returns None.
	'''
	def top(self,stack):
		if stack>self._numStacks or stack<=0:
			raise IndexError()
		stackIdx = stack-1
		if not self.empty(stack):
			arrayIdx = self._stackTop[stackIdx]	
			return self._stackarray[arrayIdx]
		else:
			return None

	''' 
	resize() - resizes the stack array,
		if triggered, all stacks get twice the capacity (not only one).
	'''
	def resize(self): #TODO
		# Get previous stack info
		currArray = self._stackarray
		currStackTop = self._stackTop
		currCapacity = self._perStackCapacity
		# Reinitialize stacks with higher capacity
		self._totalCapacity = 2 * self._totalCapacity
		self._perStackCapacity = 2 * self._perStackCapacity
		self._stackarray = [None] * self._totalCapacity
		self._stackTop = [None] * self._numStacks
		self._stackSize = [0] * self._numStacks			
		for s in range(self._numStacks):
			if currStackTop[s] is not None:
				startIdx = s * currCapacity
				endIdx = currStackTop[s]+1
				for idx in range(startIdx,endIdx):
					self.push(currArray[idx],s+1)

	''' 
	printStacks() - prints out stacks (for debugging purposes)
	'''
	def printStacks(self):
		for s in range(self._numStacks):
			print "Stack " + str(s+1) +":"
			startIdx = s*self._perStackCapacity
			endIdx = s*self._perStackCapacity + self._perStackCapacity
			print self._stackarray[startIdx:endIdx]		


'''
sts = MultiStack(4)	
sts.push(1,1)
sts.push(2,1)
sts.push(3,1)
sts.push(4,1)
sts.push(5,1)
sts.push(6,1)
sts.push(7,1)
sts.push(8,1)
sts.push(9,1)
sts.push(10,1)
sts.printStacks()
sts.push(11,1)
sts.push(12,1)
sts.printStacks()	
'''