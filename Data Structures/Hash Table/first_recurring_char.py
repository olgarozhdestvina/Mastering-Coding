arr1 = [2,5,1,2,3,5,1,2,4] # 2

arr2 = [2,10,10,2,3,5,1,2,4] # 1

arr3 = [1,2,3,4,5] # none

def first_recuring_num(arr1):
    dict = {}
    for i, val in enumerate(arr1):
        if val in dict.values():
            return val
        dict[i] = val
    return None

# O(n) - > time
# O(n) - > space

print(first_recuring_num(arr1))
print(first_recuring_num(arr2))
print(first_recuring_num(arr3))