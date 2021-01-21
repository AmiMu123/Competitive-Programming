/**
 * @param {string[]} logs
 * @return {number}
 */
var minOperations = function(logs) {
    if(logs.length ===0){
        return 0;
    }
       let backOp = '../';
       let remain = './';
       let count = 0;
       for(let i = 0;i<logs.length;i++){
           if(logs[i] !== backOp && logs[i] !== remain){
               count++;
               console.log(count,logs[i]);
           }
           else if(logs[i] ===backOp){
               if(count >0){
                   
               
   
               count = count -1;
               }
               
               console.log(count,logs[i])
               
           }
        
          
       }
       return count;
       
       
   };
   
   