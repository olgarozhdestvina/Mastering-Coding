def merge_sorted_arrays(arr1, arr2):
    if type(arr1) is list and type(arr2) is list:
        if len(arr1) == 0:
            return arr2
        elif len(arr2) == 0:
            return arr1
        return sorted(arr1 + arr2)


arr1 = [0,3,4,31]
arr2 = [4,6,30]

print(merge_sorted_arrays(arr1, []))
