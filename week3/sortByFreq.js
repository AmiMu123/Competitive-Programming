/**
 * @param {number[]} nums
 * @return {number[]}
 */
var frequencySort = function(nums) {
    let map = new Map();
    for(let i = 0;i<nums.length;i++){
        let elem = nums[i];
        let freq = map.get(elem) || 0;
        map.set(elem,freq +1);
        
}
    let freqArray = []
    let result = []
    for(let elem of map){
        freqArray.push(elem)
        
}  
 for(let i = 0;i<freqArray.length;i++){
     
 }
    
};

console.log(frequencySort([1,1,2,2,2,3]))