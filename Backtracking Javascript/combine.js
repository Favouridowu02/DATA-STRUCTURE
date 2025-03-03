const combine = function(n, k) {
    let res = [];
    function helper(start, curr){
        // base case
        if (curr.length === k) {
            res.push([...curr])
            return;
        }
        let need = k - curr.length;
        for (let j = start; j <= n - need + 1; j++) {
            curr.push(j);
            helper(j + 1, curr);
            curr.pop();
        }

        // recursive case
    }
    helper(1, []);
    return res;
}