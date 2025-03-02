/**
 * 
 * @param {numbers[]} array - The array to be rotated
 * @param {*} k - The number of Rotation
 * @returns 
 */
const rotateArray = function (array,k){
    if (array.length > 1) {
        // k = (array.length)% k;
        for (let i = 0; i < k; i++) {
            array.unshift(array.pop());
        }
    }
    return array;
}

a = [ 2, 5, 6]
k = 2;

console.log(rotateArray(a, k));