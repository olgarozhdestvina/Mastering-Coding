// If the list is sorted
// O(n log(n))

function binarySearch(arr, low, high, x) {
    if (high >= low) {
        let mid = Math.floor((high + low) / 2);
        if (arr[mid] == x) {
            return mid;
        }
        else if (arr[mid] > x) {
            return binarySearch(arr, low, mid - 1, x);
        }
        else {
            return binarySearch(arr, mid + 1, high, x);
        }
    }
    else {
        return false;
    }
}

let arr = [1,2,3,4,5,6,45,56,67,78];
binarySearch(arr, 0, arr.length-1, 45);