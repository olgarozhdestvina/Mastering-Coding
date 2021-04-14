class Stack:
    def __init__(self):
        self.array = []
        
    # see the very top node
    def peek(self):
        if len(self.array) == 0:
            return None
        return self.array[len(self.array)-1]


    # add node to the top of the stck
    def push(self, value):
        self.array.append(value)
        return self


    # remove the top node from the stack
    def pop(self):
        self.array.pop()
        return self

    # check if it it empty
    def is_empty(self):
        if len(self.array) == 0:
            return True
        return False


my_stack = Stack()
my_stack.push('google')
my_stack.push('udemy')
my_stack.push('youtube')
print(my_stack.array)
print(my_stack.is_empty())
print(my_stack.peek())
my_stack.pop()
print(my_stack.peek())
my_stack.pop()
my_stack.pop()
print(my_stack.is_empty())
print(my_stack.peek())

