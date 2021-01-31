/**
 * @param {string} S
 * @return {string}
 */
var removeDuplicates = function(S) {
    let array = []
    for(let i = 0;i<S.length ; i++){
        array.push(S[i])
    }
    let stack = [];
    while(array.length !==0){
        if(array[array.length-1] !== stack[stack.length-1]){
            stack.push(array[array.length - 1]);
            array.pop(); 
        }
       else if(array[array.length-1] === stack[stack.length-1]){
           
           stack.pop();
           array.pop();
       }
    };
    
    return stack.reverse().join("");
}