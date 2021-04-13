function mergeSortedArrays(arr1, arr2) {
    const mergedArray = [];
    let array1Item = arr1[0];
    let array2Item = arr2[0];
    let i = 1;
    let j = 1;

    if (arr1.length === 0) {
        return arr2;
    }

    if (arr2.length === 0) {
        return arr1;
    }

    else {
        while (array1Item || array2Item) {
            if (!array2Item || array1Item < array2Item) {
                mergedArray.push(array1Item);
                array1Item =arr1[i];
                i++;
            } else {
                mergedArray.push(array2Item);
                array2Item =arr2[j];
                j++;
            }
        }
    }
    return mergedArray;
}
    


arr1 = [0,3,4,31]
arr2 = [4,6,30]
mergeSortedArrays(arr1, arr2);