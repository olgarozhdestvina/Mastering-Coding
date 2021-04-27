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

    // Insert a new node
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

    // Search the tree for a value
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

    // Remove a node
    remove(value) {
        if (!this.root) {
            return false;
        }

        // Find a number and its succesor 
        let currentNode = this.root;
        let parentNode = null;

        while(currentNode){
            if(value < currentNode.value){
            parentNode = currentNode;
            currentNode = currentNode.left;
            } else if(value > currentNode.value){
            parentNode = currentNode;
            currentNode = currentNode.right;
            } else if (currentNode.value === value) {
            // If there a match.
            
            // CASE 1: No right child: 
            if (currentNode.right === null) {
                if (parentNode === null) {
                this.root = currentNode.left;
                } else {
                
                //if parent > current value, make current left child a child of parent
                if(currentNode.value < parentNode.value) {
                    parentNode.left = currentNode.left;
                
                //if parent < current value, make left child a right child of parent
                } else if(currentNode.value > parentNode.value) {
                    parentNode.right = currentNode.left;
                }
                }
            
            //CASE 2: Right child which doesnt have a left child
            } else if (currentNode.right.left === null) {
                currentNode.right.left = currentNode.left;
                if(parentNode === null) {
                this.root = currentNode.right;
                } else {
                
                //if parent > current, make right child of the left the parent
                if(currentNode.value < parentNode.value) {
                    parentNode.left = currentNode.right;
                
                //if parent < current, make right child a right child of the parent
                } else if (currentNode.value > parentNode.value) {
                    parentNode.right = currentNode.right;
                }
                }
            
            //CASE 3: Right child that has a left child
            } else {
    
                //find the Right child's left most child
                let leftmost = currentNode.right.left;
                let leftmostParent = currentNode.right;
                while(leftmost.left !== null) {
                leftmostParent = leftmost;
                leftmost = leftmost.left;
                }
                
                //Parent's left subtree is now leftmost's right subtree
                leftmostParent.left = leftmost.right;
                leftmost.left = currentNode.left;
                leftmost.right = currentNode.right;
    
                if(parentNode === null) {
                this.root = leftmost;
                } else {
                if(currentNode.value < parentNode.value) {
                    parentNode.left = leftmost;
                } else if(currentNode.value > parentNode.value) {
                    parentNode.right = leftmost;
                }
                }
            }
            return true;
            }
        }
    // If value is not found
    return false;
    }

    // Search for a node
    breadthFirstSearch() {
        // start with the root
        let currentNode = this.root;
        console.log(currentNode);

        // answer
        let list = [];

        // to keep track of children
        let queue = [];
        queue.push(currentNode);

        while (queue.length > 0) {
            currentNode = queue.shift();
            list.push(currentNode.value);

            if (currentNode.left) {
                queue.push(currentNode.left);
            }

            if (currentNode.right) {
                queue.push(currentNode.right);
            }
        } return list;
    }

    // Search for a node recursively
    breadthFirstSearchRecursive(queue, list) {
        if (!queue.length) {
            return list;
        }

        let currentNode = queue.shift();
        list.push(currentNode.value);
        if (currentNode.left) {
            queue.push(currentNode.left);
        }

        if (currentNode.right) {
            queue.push(currentNode.right);
        }
        return this.breadthFirstSearchRecursive(queue, list);
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
tree.breadthFirstSearch();
tree.breadthFirstSearchRecursive([tree.root], []);