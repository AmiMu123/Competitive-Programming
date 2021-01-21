function digitSum(n,k) {
   return superDigit(n,k);

}

function superDigit(n,k){
    // let k = 3;
    if(n.length === 1){
        return n;
    }
    else{
        let sum = 0;
        let len = n.length;
        for(let i = 0;i<len;i++){
            sum = sum + Number(n[i]);       
        }
        sum = sum * k
        sum = String(sum);
        
        k = 1;
        return superDigit(sum,k);
    }
}
console.log(digitSum('148',3));