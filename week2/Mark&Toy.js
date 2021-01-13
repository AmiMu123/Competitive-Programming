function maximumToys(prices, k) {
    let sorted = prices.sort(function(a,b){return (a-b)})
    // console.log(sorted)
    let sum = 0;
    let bought = []
    for(let i = 0;i<sorted.length;i++){
        sum += sorted[i];
        if(sum <=k){
            bought.push(sorted[i])
        }
    }
    return bought.length
    
    }
    