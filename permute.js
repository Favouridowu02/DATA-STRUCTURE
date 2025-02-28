const permute = function(nums) {
    const result = [];
    let n = nums.length;
    function helper(i) {
        // Base case
        if (i === n - 1) {
            result.push([...nums]);
            return;
        }
        // Recursive function
        for (let j = i; j < n; j++) {
            [nums[i], nums[j]] = [nums[j], nums[i]];
            helper(i + 1);
            // backtracking
            [nums[i], nums[j]] = [nums[j], nums[i]];
        }
    }
    helper(0);
    return result;
}