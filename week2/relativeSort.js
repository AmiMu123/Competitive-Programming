var relativeSortArray = function(arr1, arr2) {
    arr1 = arr1.sort(function(a,b){return a-b})
    
    let map_1 = new Map();
    let result = [];
    for(let i = 0;i<arr1.length;i++){
        let count = map_1.get(arr1[i]) || 0;
        map_1.set(arr1[i],count+1)

    }
    for( k = 0;k<arr2.length;k++){
        for(j = 0;j<map_1.get(arr2[k]);j++){
            result.push(arr2[k]);
        }
        
    }
//  return result;
// console.log(map_1);
    for(i of map_1.keys()){
        if(!arr2.includes(i)){
            for(let j = 0;j<map_1.get(i);j++){
                result.push(i)
            }
        }
    }
    return result;
    
    
};

console.log(relativeSortArray([2,21,43,38,0,42,33,7,24,13,12,27,12,24,5,23,29,48,30,31],[2,42,38,0,43,21]));