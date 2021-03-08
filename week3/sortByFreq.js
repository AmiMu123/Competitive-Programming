/**
 * @param {number[]} nums
 * @return {number[]}
 */
/*
[1,1,2,2,2,3]
 0.  1.   2. 3  
[[], [4, 3], [1], [2]...]
*/
var frequencySort = function (nums) {
    let map = new Map();
    let count = [];
    let result = []

    for (let i = 0; i < 101; i++) {
        count.push([])
    }

    for (let i = 0; i < nums.length; i++) {
        let elem = nums[i];
        let freq = map.get(elem) || 0;
        map.set(elem, freq + 1);
    }
    console.log(map, 'map items')

    for (let elem of map) {
        // console.log(elem, 'just elem')
        // console.log(elem[0], 'elem keys')
        
        count[elem[1]].push(elem[0])
    }
    console.log(count)

    for (let i = 0; i < count.length; i++) {
        if (count[i].length !== 0) {
            count[i].sort(function (a, b) {
                return b - a
            });
            for (let j = 0; j < count[i].length; j++) {
                for (let k = 0; k < i; k++) {
                    result.push(count[i][j])
                }
            }
        }
    }

    return result;

};

console.log(frequencySort([1, 1, 2, 2, 2, 3, 4]));