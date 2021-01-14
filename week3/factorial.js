function factorial(n) {
    if(n<=1){
        return 1;
    }
    else{
        return n * factorial(n-1);
    }

}
console.log(factorial(1))   //1
console.log(factorial(0))  //0
console.log(factorial(5));  // 120