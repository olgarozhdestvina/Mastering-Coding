// apples
//8947 --> grapes
//          8742 --> pears
//                    372 --> null

let myLinkedList = {
    head: {
        value: 10,
        next: //pointer to the next 
        {value: 5,
            next: {
                value: 16,
                next: {
                    value: null
                }
            }
        }
    }
}

class LinkedList {
    constructor(value) {
        this.head = {
            value: value,
            next: null
        }

        this.tail = this.head;
        this.length = 1;
    }

    printList() {
        const array = [];
        let currentNode = this.head;

        while (currentNode !== null) {
            array.push(currentNode.value);
            currentNode = currentNode.next;
        }
        return array;
    }

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
    }}
}



//console.log(myLinkedList);
const myLinkedList2 = new LinkedList(10);
myLinkedList2.append(5);
myLinkedList2.append(16);
myLinkedList2.prepend(1);
myLinkedList2.insert(2, 99);