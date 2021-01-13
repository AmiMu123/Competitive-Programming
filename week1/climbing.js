
function climbingLeaderboard(scores, alice) {
    let hash_map = new Map();
    let rank = 1;
    // time complexity O(n) time(where n is scores length)
    for(let i = 0;i<scores.length;i++){
             if(!hash_map.has(scores[i])){
                 hash_map.set(scores[i],rank++)
             }
    }
    var  find = function(hash_map,scores,alice_score){
        let left = 0;
        let right = scores.length -1;
        // O(log n) time binary search to find the position for alice score
        while(left<=right){
            let mid = Math.floor((left+right)/2);
            if(alice_score ===scores[mid]){
                return hash_map.get(alice_score);
            }
            else if(alice_score < scores[mid]){
                left = mid + 1;
                
            }
            else{
                right = mid -1;
            }
        }
        if(right<0){
            return 1;
        }
        return hash_map.get(scores[right]) +1   
    }

    
    let result_array = [];
    // O(n) time
    for(let i = 0;i<alice.length;i++){
        result_array.push(find(hash_map,scores,alice[i]));
    }
    return result_array;
}
console.log(climbingLeaderboard([100, 100 ,50 ,40 ,40 ,20 ,10],[5 ,25, 50, 120]))