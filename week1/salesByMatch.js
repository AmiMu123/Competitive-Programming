function sockMerchant(n, ar) {
    var map = new Map(); 
    for(var i = 0;i<ar.length ;i++){
        var currChar = ar[i];
        var freq = map.get(currChar) || 0;
        map.set(currChar,freq+1);
}
    var count = 0;
    for(var char of map){
       if(char[1] >1){
            var paircount = Math.floor(char[1] / 2);
            count +=paircount;
}
 }
    return count;
  
    
}
