/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {
    if(n <=0){
        return 0;
}
    if(n ===1 || n ===2){
        return 1;
}
    else{
        return fib(n-1) + fib(n-2);
}
};

console.log(fib(-1));  //  0;
console.log(fib(1));   // 1
console.log(fib(2));   // 1
console.log(fib(6));  // 8