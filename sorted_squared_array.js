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

console.log(sortedSquaredArray([0, 7, 8, -1]));