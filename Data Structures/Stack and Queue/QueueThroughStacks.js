// Queue implementation through stack
class QueueThroughStack {
    constructor() {
        this.first = [];
        this.last = [];
    }

    // Peek on the first element
    peek() {
        if (this.last.length === 0 && this.first.length > 0) {
            return this.first[0];
        }
        if (this.first.length === 0 && this.last.length > 0) {
            return this.first[0];
        }
        return null;
    }

    // Add an element to the queue
    enqueue(value) {
        const length = this.first.length;
        for (let i = 0; i < length; i++) {
            this.last.push(this.first.pop());
        }
        this.last.push(value);
        return this;
    }

    // Remove the first element
    dequeue() {
        const length = this.last.length;
        for (let i = 0; i < length; i++) {
            this.first.push(this.last.pop());
        }
        this.first.pop();
        return this;
    }
}

const myQueue = new QueueThroughStack();
myQueue.peek();
myQueue.enqueue('Joy');
myQueue.enqueue('Matt');
myQueue.enqueue('Pavel');
myQueue.peek();
myQueue.dequeue();
myQueue.dequeue();
myQueue.dequeue();
myQueue.peek();