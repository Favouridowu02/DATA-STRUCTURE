/**
 * This function takes an array of integers and returns a new array of the same length with the squares of the original integers also sorted in ascending order.
 * @param {*} array 
 * @returns A sorted Squared Array
 */

function sortedSquaredArray(array) {
    /**
     * Argument: array
     * Return: Sorted Array
     */
    const newArray = new Array(array.length).fill(0);
    for (let i = 0; i < array.length; i++) {
        newArray[i] = Math.pow(array[i],2);
    }
    newArray.sort(function(a, b) {return(a - b)});
    return newArray;
}