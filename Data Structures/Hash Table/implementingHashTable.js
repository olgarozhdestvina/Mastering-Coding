class HashTable {
    constructor(size) {
        this.data = new Array(size);
    }
    _hash(key) {
        let hash = 0;
        for (let i=0;i<key.length; i++) {
            hash = (hash + key.charCodeAt(i) * i) % this.data.length;
        }
        return hash;
    }
    set(key, val) {
        let address = this._hash(key);
        if (!this.data[address]) {
            this.data[address] = [];
        }
        this.data[address].push([key, val]);
        return this.data
    }

    get(key) {
        let address = this._hash(key);
        const currentBucket = this.data[address];
        if (currentBucket) {
            for(let j=0; j < currentBucket.length; j++) {
                if(currentBucket[j][0] === key) {
                    return currentBucket[j][1];
                }
            } 
        }
        return undefined;
        }
    
        keys() {
            if (!this.data.length) {
                return undefined;
            }
            const keysArray = [];
            for (let k = 0; k < this.data.length; k++) {
                if(this.data[k]) {
                    if (this.data.length > 1) {
                        for (let c = 0; c < this.data[k].length; c++) {
                        keysArray.push(this.data[k][c][0])
                    }
                } else {
                    keysArray.push(this.data[k][0]);
                }
                }
            }
        return keysArray;
    }
}

const myHashTable = new HashTable(50);
myHashTable.set('grapes',10000);
myHashTable.set('apples',55);
myHashTable.set('oranges',4);
myHashTable.set('bananas',10);
//myHashTable.get('grapes');
myHashTable.keys();
myHashTable.data;
