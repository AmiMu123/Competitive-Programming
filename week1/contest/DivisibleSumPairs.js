function divisibleSumPairs(n, k, ar) {
    var count = 0;
    ar = ar.sort();

    //k = 3
    for(var i = 0;i<ar.length;i++){
        for(var j = i+1;j<ar.length;j++){
            if((ar[i] + ar[j]) % k ===0){
                count = count +1;
                
            }
            
        }
        
    }
    return count

    

}

console.log(divisibleSumPairs(6,3,[1 ,3 ,2 ,6 ,1 ,2]))