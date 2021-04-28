# Breadth First Search and Depth First Search

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a new node
    def insert(self, value):
        new_node = {
            'value': value,
            'left': None,
            'right': None
        }

        if not self.root:
            self.root = new_node

        else:
            current_node = self.root

            while True:
                if value < current_node['value']:
                    # Going left
                    if not current_node['left']:
                        current_node['left'] = new_node
                        break
                    current_node = current_node['left']
                else:
                    # Going right
                    if not current_node['right']:
                        current_node['right'] = new_node
                        break
                    current_node = current_node['right']
        return self


    # Search the tree for a value
    def lookup(self, value):
        if not self.root:
            return None

        current_node = self.root

        while current_node:
            if value < current_node['value']:
                # Going left
                current_node = current_node['left']
            elif value > current_node['value']:
                # Going right
                current_node = current_node['right']
            elif current_node['value'] == value:
                return current_node
        return f'{value} not found'


    # Remove a node
    def remove(self, value):
        if not self.root:
            return False

        # Find a number and its succesor 
        current_node = self.root
        parent_node = current_node

        while current_node:
            if value < current_node['value']:
                parent_node = current_node
                current_node = current_node['left']
            elif value > current_node['value']:
                parent_node = current_node
                current_node = current_node['right']
            # if a match
            elif current_node['value'] == value:
           
            # CASE 1: No right child:
                if current_node['right'] == None:
                    if parent_node == None:
                        self.root = current_node['left']
                    else:
                        # if parent > current value, make current left child a child of parent
                        if current_node['value'] < parent_node['value']:
                            parent_node['left'] = current_node['left']

                        # if parent < current value, make left child a right child of parent
                        elif current_node['value'] > parent_node['value']:
                            parent_node['right'] = current_node['left']
                    return f'{value} was removed'

                # CASE 2: Right child doesn't have a left child
                elif current_node['right']['left'] == None:
                    current_node['right']['left'] = current_node['left']

                    if parent_node == None:
                        self.root = current_node['right']
                    else:
                        # if parent > current, make right child of the left the parent
                        if current_node['value'] < parent_node['value']:
                            parent_node['left'] = current_node['right']

                        # if parent < current, make right child a right child of the parent
                        elif current_node['value'] > parent_node['value']:
                            parent_node['right'] = current_node['right']
                    return f'{value} was removed'

                # CASE 3: Right child that has a left child
                else:

                    # find the Right child's left most child
                    leftmost = current_node['right']['left']
                    leftmost_parent = current_node['right']
                    
                    while leftmost['left'] != None:
                        leftmost_parent = leftmost
                        leftmost = leftmost['left']

                    # Parent's left subtree is now leftmost's right subtree
                    leftmost_parent['left'] = leftmost['right']
                    leftmost['left'] = current_node['left']
                    leftmost['right'] = current_node['right']

                    if parent_node == None:
                        self.root = leftmost
                    else:
                        if current_node['value'] < parent_node['value']:
                            parent_node['left'] = leftmost
                        elif current_node['value'] > parent_node['value']:
                            parent_node['right'] = leftmost
                    return f'{value} was removed'
        # if value not found 
        return f'{value} not found'
            
    # Memmory consumption is big - if the tree is wide, don't use it
    def breadth_first_seacrh(self):
        # start with the root
        current_node = self.root
        l = [] # answer
        queue = [] # to keep track of children
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            l.append(current_node['value'])

            if current_node['left']:
                queue.append(current_node['left'])
            if current_node['right']:
                queue.append(current_node['right'])

        return l


    def breadth_first_seacrh_recursive(self, queue, l):
        if not len(queue):
            return l

        current_node = queue.pop(0)
        l.append(current_node['value'])

        if current_node['left']:
            queue.append(current_node['left'])
        if current_node['right']:
            queue.append(current_node['right'])

        return self.breadth_first_seacrh_recursive(queue, l)

    # In-order -> [1, 4, 6, 9, 15, 20, 170]
    def depth_first_search_in_order(self):
        return traverse_in_order(self.root, [])

    # Pre-order -> [9, 4, 1, 6, 20, 15, 170] - Tree recreation 
    def depth_first_search_pre_order(self):
        return traverse_pre_order(self.root, [])

    # Post-order -> [1, 6, 4, 15, 170, 20, 9] - children before parent
    def depth_first_search_post_order(self):
        return traverse_post_order(self.root, [])

def traverse_in_order(node, l):
    if node['left']:
        traverse_in_order(node['left'], l)
    l.append(node['value'])

    if node['right']:
        traverse_in_order(node['right'], l)

    return l

def traverse_pre_order(node, l):
    l.append(node['value'])

    if node['left']:
        traverse_pre_order(node['left'], l)

    if node['right']:
        traverse_pre_order(node['right'], l)

    return l

def traverse_post_order(node, l):
    
    if node['left']:
        traverse_post_order(node['left'], l)

    if node['right']:
        traverse_post_order(node['right'], l)
    l.append(node['value'])

    return l




if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.insert(9)
    tree.insert(4)
    tree.insert(6)
    tree.insert(20)
    tree.insert(170)
    tree.insert(15)
    tree.insert(1)
    print('BFS', tree.breadth_first_seacrh())
    print('BFS recursive', tree.breadth_first_seacrh_recursive([tree.root], []))
    print('DFS in-order', tree.depth_first_search_in_order())
    print('DFS pre-oder', tree.depth_first_search_pre_order())
    print('DFS post-oder', tree.depth_first_search_post_order())