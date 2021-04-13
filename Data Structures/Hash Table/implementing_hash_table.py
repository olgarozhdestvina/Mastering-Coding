class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size


    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % self.size
        return hash

    def set(self, key, value):
        address = self._hash(key)
        if not self.data[address]:
            self.data[address] = []
        self.data[address].append([key,value])
        return self.data

    def get(self, key):
        address = self._hash(key)
        curr_bucket = self.data[address]
        
        if curr_bucket:
            for i in range(len(curr_bucket)):
                if curr_bucket[i][0] == key:
                    return curr_bucket[i][1]  

    def keys(self): # THE PROBLEM! you have to loop for the full length of data
        key_array = []
        for i in range(len(self.data)):
            if self.data[i] and len(self.data[i]):
                if len(self.data) > 1:
                    for j in  range(len(self.data[i])):
                        key_array.append(self.data[i][j][0])
                else:
                    key_array.append(self.data[i][0])
        return key_array
        



my_hash_table = HashTable(50)
my_hash_table.set('grapes',10000)
my_hash_table.set('apples',54)
my_hash_table.get('grapes')
my_hash_table.set('oranges',4)
my_hash_table.set('bananas', 10)

# grapes and bananas are stored in the same address
# so it is hash collision 

print(my_hash_table.keys()) 

