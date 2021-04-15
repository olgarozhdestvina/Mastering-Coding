# Stack implementation using a linked list
# LIFO

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
    

    # See the very top node
    def peek(self):
        return self.top


    # Add node to the top of the stck
    def push(self, value):
        new_node = {
            'value': value,
            'next': None
        }
        if self.is_empty():
            self.bottom = new_node
            self.top = new_node
        else:
            holding_pointer = self.top
            self.top = new_node
            self.top['next'] = holding_pointer
        self.length += 1
        return self


    # Remove the top node from the stack
    def pop(self):
        if not self.top:
            return None
        elif self.top == self.bottom:
            self.bottom = None

        else:
            self.top = self.top['next']
        self.length-=1
        return self

    # Check if it it empty
    def is_empty(self):
        if not self.bottom:
            return True
        return False

    

# Print outs
my_stack = Stack()
my_stack.push('google')
my_stack.push('udemy')
my_stack.push('youtube')
print(my_stack.is_empty())
print(my_stack.peek())
my_stack.pop()
my_stack.pop()
my_stack.pop()
print(my_stack.peek())
print(my_stack.is_empty())

