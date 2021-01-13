var intersection = function(nums1, nums2) {
    var filteredArray = nums1.filter(function(n) {
     return nums2.indexOf(n) !== -1;
 });
     let map = new Map();
     for(let i = 0;i<filteredArray.length;i++){
         let count = map.get(filteredArray[i]) || 0;
         map.set(filteredArray[i],count+1)
 }
      let res = [];
     for(let i of map.keys()){
         res.push(i)
     }
     return res;
      
     
 };