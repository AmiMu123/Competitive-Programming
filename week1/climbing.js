function climbingLeaderboard(scores, alice) {
    
    let score_map = new Map();
    let score = [];
    for(let i = 0;i<scores.length;i++){
        let elem = scores[i];
        let count = score_map.get(elem) || 0;
        score_map.set(elem,count+1);
        
    }
    for(let ranks of score_map.keys()){
        score.push(ranks);
    }

    
    let result_array = [] 
    
    for(let i = 0;i<score.length;i++){  
        
        for(let j = 0;j<alice.length;j++){ 
            
            score.push(alice[j])
            let toCheckScore = score.sort(function(a,b){return b-a});
            let result_score = toCheckScore.indexOf(alice[j]) +1;
            result_array.push(result_score);
            score.splice(toCheckScore.indexOf(alice[j]),1)
        }
       
        
        }
        
    var ans = result_array.splice(0,alice.length);
    return ans
    
}
   