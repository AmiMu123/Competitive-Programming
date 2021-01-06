function twoStacks(x, a, b) {
    let a_stack = a.reverse();
    let b_stack = b.reverse();
    let possible_lists = [];
    let sum = 0; 
    while(sum<=x){
        let top_a = a_stack[a_stack.length-1];
        let top_b = b_stack[b_stack.length-1];
        if(top_a>top_b){
            var checked_b = b_stack.pop()
            sum+=checked_b;
            if(sum<=x){
                possible_lists.push(checked_b);
            }        }
        else if(top_b>top_a){
            var checked_a = a_stack.pop();
            sum+=checked_a;
            if(sum<=x){
                possible_lists.push(checked_a)
            }
        }
        else if(top_a === top_b){
            var checked_a = a_stack.pop();
            sum+=checked_a;
            if(sum<=x){
                possible_lists.push(checked_a)
            }
        }
        else{
            if(a_stack.length ===0){
                var checked_b = b_stack.pop();
                sum+=checked_b;
                if(sum<=x){
                    possible_lists.push(checked_b);
                }

            }
            else if(b_stack.length ===0){
                var checked_a = a_stack.pop();
                sum+=checked_a;
                if(sum<=x){
                    possible_lists.push(checked_a);
                }

            }
        }
        
        

 
    
        
}
console.log(possible_lists)
return possible_lists.length
 
}

console.log(twoStacks(1000,[4 ,8 ,4 ,5],[1, 6, 1, 1 ,0 ,6 ,1 ,2, 7 ,4 ,6 ,1 ,9, 4]))
    
    
    