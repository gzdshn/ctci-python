## CTCI - Stacks and Queues Question 7
## Implement animal shelter

class Animal():
	def __init__(self,type):
		self._type = type
		self._arrivalTime = -1

	def type(self):
		return self._type

	def setTime(self,arrival):
		self._arrivalTime = arrival

	def arrivalTime(self):
		return self._arrivalTime

class AnimalShelter():
	def __init__(self):
		self._catqueue = []
		self._dogqueue = []
		self._arrivalTime = 0

	def empty(self):
		if len(self._catqueue) == 0 and len(self._dogqueue) == 0 :
			return True
		else:
			return False

	def size(self):
		return len(self._catqueue) + len(self._dogqueue)

	def enqueue(self,animal):
		animal.setTime(self._arrivalTime)
		if animal.type() == 'Cat':
			self._catqueue.append(animal)
			self._arrivalTime += 1
		elif animal.type() == 'Dog':
			self._dogqueue.append(animal)
			self._arrivalTime += 1

	def dequeueAny(self):
		cat = None
		dog = None
		if len(self._catqueue) > 0:
			cat = self._catqueue[0]
		if len(self._dogqueue) > 0:
			dog = self._dogqueue[0]
		if cat is None or dog is None:
			if cat:
				return self._catqueue.pop(0)
			elif dog:
				return self._dogqueue.pop(0)
			else:
				return None
		else:
			if cat.arrivalTime() < dog.arrivalTime():
				return self._catqueue.pop(0)
			else:
				return self._dogqueue.pop(0)

	def dequeueCat(self):
		if len(self._catqueue) > 0:
			return self._catqueue.pop(0)

	def dequeueDog(self):
		if len(self._dogqueue) > 0:
			return self._dogqueue.pop(0)

'''
shelter = AnimalShelter()
cat1 = Animal('Cat')
cat2 = Animal('Cat')
cat3 = Animal('Cat')
dog1 = Animal('Dog')
dog2 = Animal('Dog')
shelter.enqueue(cat1)
shelter.enqueue(dog1)
shelter.enqueue(dog2)
shelter.enqueue(cat2)
shelter.enqueue(cat3)
print shelter.dequeueAny().type()
print shelter.dequeueAny().type()
print shelter.dequeueCat().type()
print shelter.dequeueDog().type()
print "Size: " + str(shelter.size())
'''
