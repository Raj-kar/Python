class Stack:
	def __init__(self):
		self.data = []

	def push(self, value):
		self.data.append(value)

	def pop(self):
		if(len(self.data) != 0):
			self.data.pop()
		else:
			return "Underflow"

	def peek(self):
		return self.data[len(self.data) - 1]

	def isEmpty(self):
		if(len(self.data) == 0):
			return True
		else:
			return False


myStack = Stack()
myStack.push(10)
myStack.push(6)
myStack.push(20)
myStack.push(16)
print(myStack.data)
print(myStack.isEmpty())
myStack.pop()
myStack.pop()
print(myStack.data)
print(myStack.peek())