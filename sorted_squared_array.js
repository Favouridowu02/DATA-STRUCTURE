/**
 * Returns a new array containing the squares of each number in the input array, sorted in ascending order.
 * 
 * @param {numbers[]} array - An array of integers
 * @returns {numbers[]} A new array of the same length containing the squared values, sorted in ascending order.
 */

function sortedSquaredArray(array) {
    // Create an array of the same length, initialized with zeros
    const newArray = new Array(array.length).fill(0);
    // Square each element and store in the new array
    for (let i = 0; i < array.length; i++) {
        newArray[i] = Math.pow(array[i],2);
    }
    // Sort the squared values in ascending order
    newArray.sort((a, b) => a - b);
    return newArray;
}


function sortedSquared(array) {
    // This is an optimised version
    const newArray = new Array(array.length).fill(0);
    leftPointer = 0;
    rightPointer = array.length - 1;
    for (let i = array.length - 1; i >= 0; i--) {
        const leftSquared = Math.pow(array[leftPointer], 2)
        const rightSquared = Math.pow(array[rightPointer], 2)
        if (leftSquared > rightSquared) {
            newArray[i] = leftSquared;
            leftPointer++;
        } else {
            newArray[i] = rightSquared;
            rightPointer--;
        }
    }
    return newArray;
}

a = [1, 4, 5, 7]
b = [-6, -1, 0, 8, 10]
c = []
console.log(sortedSquared(a));
console.log(sortedSquared(b));
console.log(sortedSquared(c));