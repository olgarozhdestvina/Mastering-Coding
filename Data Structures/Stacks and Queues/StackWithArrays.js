class Stack {
    constructor() {
        this.array = [];
    }

    // see the very top node
    peek(){
        if(this.array.length == 0) {
            return null;}
        return this.array[this.array.length-1];
        
    }

    // add node to the top of the stck
    push(value){
        this.array.push(value);
        return this;
    }

    // remove the top node from the stack
    pop(){
        this.array.pop();
        return this;
    }

    // check if it it empty
    isEmpty() {
    if (!this.array) {
        return true; }
    return false;

    }
}

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