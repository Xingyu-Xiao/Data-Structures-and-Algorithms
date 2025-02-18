class Node:
	def __init__(self, data, next=None):
		self.data, self.next = data, next

class LinkList:
	def __init__(self):
		self.head = None

	def initList(self, data):
		self.head = Node(data[0])
		p = self.head
		for i in data[1:]:
			node = Node(i)
			p.next = node
			p = p.next

	def insertCat(self):
		g = Node(6)
		p = self.head
		n = 0
		while p:
			p = p.next
			n += 1
		nn = n//2 if n%2 == 0 else n//2+1
		p = self.head
		for i in range(nn-1):
			p = p.next
		f = p.next
		p.next = g
		g.next = f

	def printLk(self):
		p = self.head
		while p:
			print(p.data, end=" ")
			p = p.next
		print()

lst = list(map(int, input().split()))
lkList = LinkList()
lkList.initList(lst)
lkList.insertCat()
lkList.printLk()
