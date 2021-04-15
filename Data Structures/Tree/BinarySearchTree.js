// Binary Search Tree 
// Left child - always descreses; right - always increases
// Balances (O(log n)) vs unbalances (could become O(n))

class Node {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

class BinarySearchTree {
    constructor() {
        this.root = null;
    }

    insert(value) {
        const newNode = new Node(value);
        if (this.root === null) {
            this.root = newNode;
        } else {
            let currentNode = this.root;
            while (true) {
                if (value < currentNode.value) {
                    //Left
                    if (!currentNode.left) {
                        currentNode.left = newNode;
                        return this;
                    }
                    currentNode = currentNode.left;
                } else {
                    //Right
                    if (!currentNode.right) {
                        currentNode.right = newNode;
                        return this;
                    }
                    currentNode = currentNode.right;
                }
            }
        }
    }

    lookup(value) {
        if (!this.root) {
            return null;
        }
        let currentNode = this.root;

        while (currentNode) {
            if (value < currentNode.value) {
                // Going left
                currentNode = currentNode.left;
                }
            else if (value > currentNode.value) {
                // Going right
                currentNode = currentNode.right;
                }
            else if (currentNode.value == value ){
                return currentNode;
            }
        }
        return null;
    }

    remove(value) {
        let currentNode = this.lookup(value);
        let parentNode = null;
        }
    }
}


function traverse(node) {
    const tree = { value: node.value };
    tree.left = node.left === null ? null : traverse(node.left);
    tree.right = node.right === null ? null : traverse(node.right);
    return tree;
}



// 			    9
//	    4				20
// 1		6 		15		170

const tree = new BinarySearchTree();
tree.insert(9);
tree.insert(4);
tree.insert(6);
tree.insert(20);
tree.insert(170);
tree.insert(15);
tree.insert(1);
JSON.stringify(traverse(tree.root))
tree.lookup(170);
tree.lookup(2);
