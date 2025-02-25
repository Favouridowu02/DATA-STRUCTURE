/**
 * 
 * @param {numbers[]} array - This is an Array of numbers
 * @returns - True is the array is monotonic decreasing or increasing else return False
 */


const checkMonotonic = function (array) {
    let return_type = ""
    if (array.length <= 1) {
        return true
    }
    for (let i = 0; i < array.length - 1; i++) {
        if (array[i] == array[i + 1]) {
            continue;
        } else if (array[i] < array[i + 1]) {
            if (return_type === "decreasing") {
                return false;
            }
            return_type = "increasing";
        } else if (array[i] > array[i + 1]) {
            if (return_type === "increasing") {
                return false;
            }
            return_type = "decreasing";
        }
    }
    return true;
}