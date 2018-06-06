## Tests For Singly Linked List Implementation
from myllist import LinkedList

list1 = LinkedList()
print "Size is: " + str(list1.size())

list1.append(1)
list1.append(2)
list1.append(3)
print "Size is: " + str(list1.size())
for idx in range(list1.size()):
	print list1.get(idx)

list1.insert(4,3)
print "Size is: " + str(list1.size())
for idx in range(list1.size()):
	print list1.get(idx)

list1.remove(3)
print "Size is: " + str(list1.size())
for idx in range(list1.size()):
	print list1.get(idx)

