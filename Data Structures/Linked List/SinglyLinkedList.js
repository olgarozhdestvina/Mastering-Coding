// Implementation of a single link list. 

class SingleLinkedList {
    constructor(value) {
        this.head = {
            value: value,
            next: null
        }

        this.tail = this.head;
        this.length = 1;
    }

    // Print the linked list
    printList() {
        const array = [];
        let currentNode = this.head;

        while (currentNode !== null) {
            array.push(currentNode.value);
            currentNode = currentNode.next;
        }
        return array;
    }

    // Appending a new node to the linked list
    append(value) {
        const newNode = {
            value: value,
            next: null
        };

        this.tail.next = newNode;
        this.tail = newNode;
        this.length++;
        return this.printList();
    }

    // Prepending a new node to the linked list
    prepend(value) {
        const newNode = {
            value: value,
            next: this.head
        };

        newNode.next = this.head
        this.head = newNode;
        this.length++;
        return this.printList();
    }

    // Find a node by its index
    traverseToIndex(index) {
        //check for params --> assuming valid
        let counter = 0;
        let currentNode = this.head;
        
        while (counter !== index) {
            currentNode = currentNode.next;
            counter++;
        }
        return currentNode;

    }

    // Insert a new node by its index 
    insert(index, value) {
        // check params
        if (index === 0) {
            this.prepend(value);
        };

        if (index >= this.length) {
            this.append(value);
        } else {

        const newNode = {
            value: value,
            next: null
        };

        const leader = this.traverseToIndex(index-1);
        const holdingPointer = leader.next;

        leader.next = newNode;
        newNode.next = holdingPointer;
        this.length++;

        return this.printList();
        }
    }

    // Remove a node by its index
    remove(index) {
        if (index === 0) {
            this.head = this.head.next;
        };

        if (index >= this.length) {
            const leader = this.traverseToIndex(this.length-2);
            leader.next = null
        } else {

            const leader = this.traverseToIndex(index-1);
            const nodeToRemove = leader.next;
            leader.next = nodeToRemove.next;
        }
        this.length--;
        return this.printList();
    }
}



// Print outs
const myLinkedList2 = new SingleLinkedList(10);
myLinkedList2.append(5);
myLinkedList2.append(16);
myLinkedList2.prepend(1);
myLinkedList2.insert(2, 99);
myLinkedList2.remove(2);
myLinkedList2.remove(20);