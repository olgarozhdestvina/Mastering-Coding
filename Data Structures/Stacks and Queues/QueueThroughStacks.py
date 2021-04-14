# Queue implementation through stack

class QueueThroughStacks: 
    def __init__(self):
        self.first = []
        self.last = []

    # Peek on the first element
    def peek(self):
        if len(self.last) == 0 and len(self.first) > 0:
            return self.first[0]
        elif len(self.last) > 0 and len(self.first) == 0:
            return self.last[0]
        return None

    # Add an element to the queue 
    def enqueue(self,value):
        l = len(self.first)
        for _ in range(l):
            self.last.append(self.first.pop())
        self.last.append(value)
        return self


    # Remove the first element
    def dequeue(self):
        l = len(self.last)
        for _ in range(l):
            self.first.append(self.last.pop())
        self.first.pop()
        return self


    
# Print outs
my_queue = QueueThroughStacks()
my_queue.peek()
my_queue.enqueue('Joy')
my_queue.enqueue('Matt')
my_queue.enqueue('Pavel')
print(my_queue.peek())
my_queue.dequeue()
print(my_queue.peek())
my_queue.dequeue()
my_queue.dequeue()
print(my_queue.peek())
