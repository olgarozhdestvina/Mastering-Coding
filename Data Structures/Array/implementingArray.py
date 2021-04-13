class MyArray():
    def __init__(self, length=0, data={}):
        self.length = length
        self.data = data
    
    def get(self,index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length +=1
        return self.length

    def pop(self):
        last_elem = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -=1
        return last_elem

    def delete(self,index):
        item = self.data[index]
        self.shift(index)
        return item

    def shift(self, index):
        while index < self.length-1:
            self.data[index] = self.data[index+1]
            index +=1
        del self.data[self.length-1]
        return self.data


my_array = MyArray()

my_array.push('hi')
my_array.push('you')
my_array.push('!')
my_array.push('!')
my_array.push('!')
my_array.push('!')
print(my_array.data)

print(my_array.get(0))
print(my_array.pop())
print(my_array.delete(1))

print(my_array.data)

