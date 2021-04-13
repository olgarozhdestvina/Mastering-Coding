linked_list = {
    'head': {
        'value': 10,
        'next': {
            'value': 5,
            'next': {
                'value': 16,
                'next': {
                    'value': None
                }
            }
        }
    }
}


class LinkedList:
    def __init__(self, value):
        self.head = {
            'value': value,
            'next': None
        }

        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = {
            'value': value,
            'next': None
        }

        self.tail['next'] = new_node
        self.tail = new_node
        self.length += 1
        return self

    def prepend(self, value):
        new_node = {
            'value': value,
            'next': self.head
        }

        new_node['next'] = self.head
        self.head = new_node
        self.length += 1
        return self

    def print_list(self):
        array = []
        current_node = self.head

        while current_node != None:
            array.append(current_node['value'])
            current_node = current_node['next']
        return array

    def traverse_to_index(self, index):
        counter = 0
        current_node = self.head

        while counter != index:
            current_node = current_node['next']
            counter += 1
        return current_node

    def insert(self, index, value):
        # Check params
        if index >= self.length:
            self.append(value)

        elif index == 0:
            self.prepend(value)

        else: 
            new_node = {
                'value': value,
                'next': None
            }

            leader = self.traverse_to_index(index - 1)
            holding_pointer = leader['next']
            leader['next'] = new_node
            new_node['next'] = holding_pointer
            self.length +=1
        return self


my_linked_list = LinkedList(10)
my_linked_list.append(5)
my_linked_list.append(16)
my_linked_list.prepend(1)
my_linked_list.insert(2, 99)
my_linked_list.insert(20, 89)
print(my_linked_list.print_list())
