// Stack implementation using a linked list
// LIFO

class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class Stack {
    constructor() {
        this.top = null;
        this.bottom = null;
        this.length = 0;
    }

    // See the very top node
    peek(){
        return this.top;
    }

    // Add a node to the top of the stck
    push(value){
        const newNode = new Node(value);
        if (this.length === 0) {
            this.top = newNode;
            this.bottom = newNode;
        } else {
            const holdingPointer = this.top;
            this.top = newNode
            this.top['next'] = holdingPointer
        }
        this.length++;
        return this;
    }

    // Remove the top node from the stack
    pop(){
        if (!this.top) {
            return null;
        }
        if (this.top === this.bottom) {
            this.bottom = null;
        }
        this.top = this.top.next;
        this.length--;
        return this;
    }

    // Check if it it empty
    isEmpty() {
    if (!this.bottom) {
        return true; }
    return false;
    }
}


// Print outs
const myStack = new Stack();
myStack.push('google')
myStack.push('udemy')
myStack.push('youtube')
myStack.peek()
myStack.isEmpty()
myStack.pop()
myStack.pop()
myStack.pop()
myStack.isEmpty()