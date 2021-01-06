function twoStacks(x, a, b) {
    let index_a = 0;
    let index_b = 0;
    let count = 0;
    let sum = 0;
    while(index_b <b.length && sum+b[index_b]<=x){ 
        sum +=b[index_b]; 
        index_b++;
    }
    count = index_b;
    index_b--;
    while(index_a<a.length && index_b<b.length){
        sum = sum+ a[index_a];
        if(sum>x){
            while(index_b >=0){
                sum = sum -b[index_b];
                index_b--;
                if(sum<=x){
                    break;
                }
            }
            if(sum > x && index_b< 0){
                index_b--;
                break;
            }
        }
    
    count = Math.max(index_a + index_b+2,count);
    index_a++;
    }
    return count;
}

console.log(twoStacks(20,[10 ,8 ,4 ,5],[17, 1, 1, 1 ,0 ,6 ,1 ,2, 7 ,4 ,6 ,1 ,9, 4]))