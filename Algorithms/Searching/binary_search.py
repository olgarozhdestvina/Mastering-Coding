# If the list is sorted
# O(n log(n))

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return False

arr = [1,2,3,4,5,6,45,56,67,78]
print(binary_search(arr, 0, len(arr)-1, 45))