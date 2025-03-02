// This module contains a function subsets that used to find
// the possible subsets using backtracking 
/**
 * 
 * @param {numbers[]} nums - an Array of numbers
 */

const powerSet = function(nums) {
    const output = [];
    const helper =  function(nums, i, subset) {
        if (i === nums.length) {
            output.push(subset.slice());
            return;
        }
        // don't add
        helper(nums, i + 1, subset);
        // add
        subset.push(nums[i]);
        helper(nums, i + 1, subset);
        subset.pop();
    }
    helper(nums, 0, []);
    return output;
}

// testing
console.log(`This is the Number of posible subsets${powerSet([1, 2, 3 ]).length}`);
console.log(powerSet([1, 2, 3 ]));


const subsetWithDup = function (nums) {
    let res = [];
    nums.sort((a, b) => a-b);
    function subsets(index, curr) {
        if (index === nums.length) {
            res.push([...curr]);
            return;
        }
        // include
        curr.push(nums[index]);
        subsets(index + 1, curr);
        curr.pop();

        // exclude 
        while(index < nums.length - 1 && nums[index] === nums[index + 1]) {
            index++;
        }
        subsets(index + 1, curr);
    }
    subsets(0, []);
    return res;
}