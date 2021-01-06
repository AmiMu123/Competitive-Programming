var twoSum = function(nums, target) {  
    var map = new Map();  // O(1)
    for(var i = 0;i<nums.length;i++){  //O(n)
      currNum = nums[i];  
      var value = target - currNum; 
        
        if(map.has(value)){
            var array = [i];
            console.log(map.get(value))
            // array.push(map.get(value))
            return array;
        }
        else{
            map.set(currNum,i)
            
        }
        
}   
    
};
console.log(twoSum([1,2,3,4,5],9));