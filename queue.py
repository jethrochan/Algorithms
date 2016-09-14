#Challenge: Implementing a Queue with 2 Stacks
class Queue():
    #initialize stacks
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enque(self, element):
        #push item onto stack 1
        self.stack1.append(element)
        
    def deque(self):
        if not self.stack2: #if stack2 empty
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


myqueue = Queue()

myqueue.enque(6)
myqueue.enque(8)
myqueue.enque(10)

print(myqueue.deque()) #prints 6


