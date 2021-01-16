var reorganizeString = function(S) {
    let hash_map = new Map();
    for(let i = 0;i<S.length;i++){
        let freq = hash_map.get(S[i]) || 0;
        hash_map.set(S[i],freq+1);
        
}
    let rep_array = []
    for(let elem of hash_map){
        rep_array.push(elem[1])
    }
    let min = rep_array[0]
    let max = rep_array[0]
    for(let i = 0; i<rep_array.length;i++){
        if(rep_array[i]<min){
            let temp = rep_array[i];
            rep_array[i] = min;
            min = temp;

        }
        else if(rep_array[i] >max){
            let temp = rep_array[i];
            rep_array[i] = max;
            max = temp;
            
        }
    
    }
    let reorganized = max -min <= 1;
    return reorganized;

    
};

console.log(reorganizeString('aba'));