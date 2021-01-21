function quickSort(arr) {
    if(arr.length <2){
        return arr;
    }
    
    let pivot = arr[0];
    let left = []
    let right =[];
    let result = [];
    for(let i = 0;i<arr.length;i++){
        if(arr[i]<pivot){
            left.push(arr[i])
        }
        else{
            right.push(arr[i])
        }
    }
       result =  left.concat(right);
       return result;     
}
