# Binary Search Tree
# Left child - always descreses right - always increases
# Balances (O(log n)) vs unbalances (could become O(n))


class BinarySearchTree:
    def __init__(self):
        self.root = None

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
        return None



    def remove(self, value):
        if not self.root:
            return None

        # locate the number and find a successor
        node_to_remove = self.root
        parent_node = None

        while node_to_remove:
            if value < node_to_remove['value']:
                # Going left
                parent_node = node_to_remove
                node_to_remove = node_to_remove['left']

            elif value > node_to_remove['value']:
                # Going right
                parent_node = node_to_remove
                node_to_remove = node_to_remove['right']

            # if match:
            elif node_to_remove['value'] == value:

               # CASE 1: No right child.
                if not node_to_remove['right']:

                    # if root
                    if not parent_node:
                        self.root = node_to_remove['left']
                        break

                        # make left child a left child of the parent node
                    elif node_to_remove['value'] < parent_node['value']:
                        parent_node['left'] = node_to_remove['left']

                        # make left child a right child of then parent node
                    elif node_to_remove['value'] > parent_node['value']:
                        parent_node['right'] = node_to_remove['left']

                # CASE 2: Right child doesn't have a left child
                elif not node_to_remove['right']['left']:
                    node_to_remove['right']['left'] = node_to_remove['left']

                    # make right child a left child of the parent node
                    if node_to_remove['value'] < parent_node['value']:
                        parent_node['left'] = node_to_remove['right']

                    # make right child a right child of then parent node
                    elif node_to_remove['value'] > parent_node['value']:
                        parent_node['right'] = node_to_remove['right']

                # Case 3: Right child has left a left child
                else:

                    # find the right child left most child
                    left_most = node_to_remove['right']['left']
                    left_most_parent = node_to_remove['right']

                    while left_most['left']:
                        left_most_parent = left_most
                        left_most = left_most['left']

                    # parent's left subtree is now left most's right subtree
                    left_most_parent['left'] = left_most['right']
                    left_most['left'] = node_to_remove['left']
                    left_most['right'] = node_to_remove['right']

                    if not parent_node:
                        self.root = left_most

                    else:
                        if node_to_remove['value'] < parent_node['value']:
                            parent_node['left'] = left_most
                        elif node_to_remove['value'] > parent_node['value']:
                            parent_node['right'] = left_most

        return True


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.insert(9)
    tree.insert(4)
    tree.insert(6)
    tree.insert(20)
    tree.insert(170)
    tree.insert(15)
    tree.insert(1)
    # print(tree.__dict__)
    tree.lookup(170)
    tree.remove(170)
    # print(tree.__dict__)
