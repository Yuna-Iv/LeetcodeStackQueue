class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        self.head = Node(item, next=self.head)

    def pop(self):
        if self.head is None:
            return
        val = self.head.val
        self.head = self.head.next
        return val

    def peek(self):
        return self.head.val

class MyQueue:
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()

    def _transfer(self):
        if self.outbox.is_empty():
            while not self.inbox.is_empty():
                self.outbox.push(self.inbox.pop())

    def push(self, x):
        self.inbox.push(x)

    def pop(self):
        self._transfer()
        return self.outbox.pop()

    def peek(self):
        self._transfer()
        return self.outbox.peek()

    def empty(self):
        return self.inbox.is_empty() and self.outbox.is_empty()



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
