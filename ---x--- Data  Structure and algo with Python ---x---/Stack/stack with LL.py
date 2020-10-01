class Node:
    """Create node for stack"""

    def __init__(self, value):
        self.data = value
        self.next = None


class Stack:
	""" LIFO --> Last in First out !"""
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def push(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.top = newNode
            self.bottom = newNode
        else:
            holdingPointer = self.top
            self.top = newNode
            self.top.next = holdingPointer
        self.length += 1

    def pop(self):
        if self.length == 0:
            return "UnderFlow"
        self.top = self.top.next

    def print_stack(self):
        if self.top == None:
            print("Stack empty")
        else:
            current_pointer = self.top
            print("Values on stack --> ", end="")
            while(current_pointer != None):
                print(current_pointer.data, end=" ")
                current_pointer = current_pointer.next

myStack = Stack()
myStack.push(10)
myStack.push(5)
myStack.push(15)
# print(myStack.top.data)
# myStack.pop()
# print(myStack.top.data)
myStack.print_stack()
