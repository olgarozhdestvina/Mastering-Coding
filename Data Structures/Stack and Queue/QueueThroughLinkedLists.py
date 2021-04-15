# Queue implementation through linked lits
# FIFO

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue(Node):
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    

    # Peek on the first node
    def peek(self):
        return self.first
    

    # Add a node to the queue
    def enqueue(self,value):
        super().__init__(value)
        new_node = Node(value)
        if self.is_empty():
            self.last = new_node
            self.first = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return self.value


    # Remove the first node
    def dequeue(self):
        if not self.last:
            return None
        elif self.first == self.last:
            self.first = None
        else:
            self.first = self.first.next

        self.length-=1
        return self

    
    # Check if the queue is empty
    def is_empty(self):
        if not self.last:
            return True
        return False

    

# Print outs
my_queue = Queue()
print(my_queue.is_empty())
my_queue.enqueue('Joy')
my_queue.enqueue('Matt')
my_queue.enqueue('Pavel')
my_queue.enqueue('Samir')
print(my_queue.peek())
my_queue.dequeue()
print(my_queue.peek())
print(my_queue.is_empty())
my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
print(my_queue.peek())
