const combinationSum = function(candidates, target) {
    let res = [];
    function combinationSumRecursive(index, curr, currSum) {
        if (currSum > target) {
            return;
        }
        if (currSum === target) {
            res.push([...curr]);
            return;
        }
        for (let j = index; j < candidates.length; j++) {
            curr.push(candidates[j]);
            combinationSumRecursive(j, curr, currSum + candidates[j]);
            curr.pop();
        }
    }
    combinationSumRecursive(0, [], 0);
    return res;
}