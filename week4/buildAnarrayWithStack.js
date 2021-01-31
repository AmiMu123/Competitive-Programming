/**
 * @param {number[]} target
 * @param {number} n
 * @return {string[]}
 */
var buildArray = function(target, n) {
    let seen = new Set();
    for(let i = 0; i<target.length ; i++){
        seen.add(target[i])
    }
    let result = []
    for(let i = 1 ; i <=n ; i++){
        if(seen.has(i)){
            result.push('Push')
            target.shift();
            if(target.length ===0){
                break;
            }
        }
        else{
        result.push('Push');
        result.push('Pop');
        }
    }
    return result;
    
};