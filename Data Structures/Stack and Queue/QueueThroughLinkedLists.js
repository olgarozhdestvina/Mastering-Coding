// Queue implementation through Linked lists
// FIFO

class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}


class Queue {
    constructor() {
        this.first = null;
        this.last = null;
        this.length = 0;
    }

    // Peek on the first node
    peek() {
        return this.first;
    }

    // Add a node to the queue
    enqueue(value) {
        const newNode = new Node(value);
        if (this.isEmpty()) {
            this.first = newNode;
            this.last = newNode;
        }
        else {
           this.last.next = newNode;
           this.last = newNode;
        }
        this.length++;
        return this
    }

    // Remove the first node
    dequeue() {
        if (!this.first){
            return null;
        }
        if (this.first === this.last) {
            this.first = null;
        }
        
        this.first = this.first.next;
        this.length--;
        return this;

    }

    // Check if the queue is empty
    isEmpty() {
        if (!this.first) {
            return true; }
        return false;
        }
}

// Print outs
const myQueue = new Queue();
myQueue.isEmpty();
myQueue.enqueue('Joy');
myQueue.enqueue('Matt');
myQueue.enqueue('Pavel');
myQueue.enqueue('Samir');
myQueue.peek();
myQueue.dequeue();
myQueue.peek();

