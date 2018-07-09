## CTCI - Stacks and Queues Question 4
## Towers of Hanoi using three stacks, uses recursion

class TowersOfHanoi:
	def __init__(self, N):
		self._stacks = [[],[],[]]
		self._N = N
		for i in range(N,0,-1):
			self._stacks[0].append(i)

	def solve(self):
		self.moveTower(self._N,0,2,1)

	def moveTower(self,height,fromTower,toTower,midTower):
		if height>0:
			self.moveTower(height-1,fromTower,midTower,toTower)
			self.moveDisk(fromTower,toTower)
			self.moveTower(height-1,midTower,toTower,fromTower)

	def moveDisk(self,fromTower,toTower):
		#print "Move from " + str(fromTower) + " to " + str(toTower)
		val = self._stacks[fromTower].pop()
		self._stacks[toTower].append(val)


toh = TowersOfHanoi(10)
toh.solve()
print toh._stacks
