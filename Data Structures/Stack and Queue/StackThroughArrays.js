// Stack implementation using an array
// LIFO

class Stack {
    constructor() {
        this.array = [];
    }

    // See the very top node
    peek(){
        if(this.array.length == 0) {
            return null;}
        return this.array[this.array.length-1];
        
    }

    // Add a node to the top of the stck
    push(value){
        this.array.push(value);
        return this;
    }

    // Remove the top node from the stack
    pop(){
        this.array.pop();
        return this;
    }

    // Check if it it empty
    isEmpty() {
    if (!this.array) {
        return true; }
    return false;

    }
}

// Print outs
const myStack = new Stack();
myStack.push('google');
myStack.push('udemy');
myStack.push('youtube');
myStack.peek();
myStack.isEmpty();
myStack.pop();
myStack.pop();
myStack.pop();
myStack.isEmpty();
myStack.peek();